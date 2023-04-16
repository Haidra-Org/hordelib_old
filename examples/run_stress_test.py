# This tests running hordelib standalone, as an external caller would use it.
# Call with: python -m test.run_stress_test
# You need all the deps in whatever environment you are running this.
import time

if __name__ != "__main__":
    exit(0)
import random

random.seed(999)

import hordelib

hordelib.initialise(setup_logging=False)

import threading

from loguru import logger
from PIL import Image

from hordelib.horde import HordeLib
from hordelib.shared_model_manager import SharedModelManager

generate = HordeLib()
SharedModelManager.loadModelManagers(compvis=True, controlnet=True)
SharedModelManager.manager.load("Deliberate")
SharedModelManager.manager.load("Anything Diffusion")
SharedModelManager.manager.load("Realistic Vision")
SharedModelManager.manager.load("Papercutcraft")

models = ["Deliberate", "Anything Diffusion", "Realistic Vision", "Papercutcraft"]
cnets = ["openpose", "canny", "fakescribbes", "hed", "depth"]

start_time = time.time()

ITERATIONS = 1
CONTROL_NET = True

mutex = threading.Lock()
count = 0


def inc():
    with mutex:
        global count
        count += 1


def generate_images():
    data = {
        "sampler_name": "k_dpmpp_2m",
        "cfg_scale": 7.5,
        "denoising_strength": 1.0,
        "seed": random.randint(1, 1000000000),
        "height": 512,
        "width": 512,
        "karras": random.random() < 0.5,
        "tiling": False,
        "hires_fix": False,
        "clip_skip": 1,
        "control_type": None,
        "image_is_control": False,
        "return_control_map": False,
        "prompt": "an ancient llamia monster",
        "ddim_steps": 25,
        "n_iter": 1,
        "model": random.choice(models),
    }
    horde = HordeLib()
    pil_image = horde.basic_inference(data)
    inc()


def generate_images_portrait():
    data = {
        "sampler_name": "k_dpmpp_2m",
        "cfg_scale": 7.5,
        "denoising_strength": 1.0,
        "seed": random.randint(1, 1000000000),
        "height": 512,
        "width": 768,
        "karras": random.random() < 0.5,
        "tiling": False,
        "hires_fix": False,
        "clip_skip": 1,
        "control_type": None,
        "image_is_control": False,
        "return_control_map": False,
        "prompt": "an ancient llamia monster",
        "ddim_steps": 25,
        "n_iter": 1,
        "model": random.choice(models),
    }
    horde = HordeLib()
    pil_image = horde.basic_inference(data)
    inc()


def generate_images_hires_fix():
    data = {
        "sampler_name": "k_dpmpp_2m",
        "cfg_scale": 7.5,
        "denoising_strength": 1.0,
        "seed": random.randint(1, 1000000000),
        "height": 768,
        "width": 768,
        "karras": random.random() < 0.5,
        "tiling": False,
        "hires_fix": True,
        "clip_skip": 1,
        "control_type": None,
        "image_is_control": False,
        "return_control_map": False,
        "prompt": "an ancient llamia monster",
        "ddim_steps": 25,
        "n_iter": 1,
        "model": random.choice(models),
    }
    horde = HordeLib()
    pil_image = horde.basic_inference(data)
    inc()


def generate_images_cnet():
    if not CONTROL_NET:
        return
    data = {
        "sampler_name": "k_dpmpp_2m",
        "cfg_scale": 7.5,
        "denoising_strength": 1.0,
        "seed": random.randint(1, 1000000000),
        "height": 512,
        "width": 768,
        "karras": random.random() < 0.5,
        "tiling": False,
        "hires_fix": False,
        "clip_skip": 1,
        "control_type": random.choice(cnets),
        "image_is_control": False,
        "return_control_map": False,
        "prompt": "a man walking in the snow",
        "ddim_steps": 25,
        "n_iter": 1,
        "model": random.choice(models),
        "source_image": Image.open("images/test_db0.jpg"),
        "source_processing": "img2img",
    }
    horde = HordeLib()
    pil_image = horde.basic_inference(data)
    inc()


def generate_images_img2img():
    data = {
        "sampler_name": "k_dpmpp_2m",
        "cfg_scale": 7.5,
        "denoising_strength": 0.4,
        "seed": random.randint(1, 1000000000),
        "height": 768,
        "width": 512,
        "karras": random.random() < 0.5,
        "tiling": False,
        "hires_fix": False,
        "clip_skip": 1,
        "control_type": None,
        "image_is_control": False,
        "return_control_map": False,
        "prompt": "a dinosaur",
        "ddim_steps": 25,
        "n_iter": 1,
        "model": random.choice(models),
        "source_image": Image.open("images/test_db0.jpg"),
        "source_processing": "img2img",
    }
    horde = HordeLib()
    pil_image = horde.basic_inference(data)
    inc()


def run_iterations():
    for i in range(ITERATIONS):
        generate_images()
        generate_images_portrait()
        generate_images_cnet()
        generate_images_img2img()
        generate_images_hires_fix()


def main():
    global count
    count = 0
    threads = [
        threading.Thread(daemon=True, target=run_iterations),
        threading.Thread(daemon=True, target=run_iterations),
        threading.Thread(daemon=True, target=run_iterations),
    ]
    [x.start() for x in threads]
    [x.join() for x in threads if x]

    expected_iterations = (ITERATIONS * 5) * len(threads)
    logger.warning(f"Test took {round(time.time() - start_time)} seconds ({count} generations)")
    if expected_iterations != count:
        logger.error("Test did not finsihed all iterations")


main()

# 275 seconds, 3 threads, 5 iterations, 5 tests = 3.6 seconds per gen
# 311 seconds, 3 threads, 5 iterations, 5 tests, 1 at a time (mutex locked) = 4.14
# 265 seconds, 3 threads, 5 iterations, 5 tests, sampler_mutex = 3.5 seconds per gen
