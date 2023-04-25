# This tests running hordelib standalone, as an external caller would use it.
# Call with: python -m test.run_memory_test
# You need all the deps in whatever environment you are running this.
import psutil
from loguru import logger
import random
import threading

import hordelib
hordelib.initialise(setup_logging=True)

from hordelib.horde import HordeLib
from hordelib.shared_model_manager import SharedModelManager
from hordelib.settings import UserSettings
from hordelib.utils.gpuinfo import GPUInfo
from hordelib.comfy_horde import cleanup


def get_ram():
    virtual_memory = psutil.virtual_memory()
    total_ram_mb = virtual_memory.total / (1024 * 1024)
    used_ram = virtual_memory.used / (1024 * 1024)
    free_ram = total_ram_mb - used_ram
    return (int(total_ram_mb), int(used_ram), int(free_ram))


def get_free_ram():
    _, _, free = get_ram()
    return free


def get_free_vram():
    gpu = GPUInfo()
    return gpu.get_free_vram_mb()


def report_ram():
    logger.warning(f"Free RAM {get_free_ram()} MB")
    logger.warning(f"Free VRAM {get_free_vram()} MB")


def add_model(model_name):
    logger.warning(f"Loading model {model_name}")
    SharedModelManager.manager.load(model_name)
    report_ram()
    model_count = len(SharedModelManager.manager.compvis.get_loaded_models_names())
    logger.warning(f"{model_count} models now loaded")


def get_available_models():
    models = SharedModelManager.manager.get_available_models()
    return models


def do_inference(model_name):
    """Do some work on the GPU"""
    horde = HordeLib()
    data = {
        "sampler_name": "k_euler",
        "cfg_scale": 7.5,
        "denoising_strength": 1.0,
        "seed": 123456789,
        "height": 512,
        "width": 512,
        "karras": True,
        "tiling": False,
        "hires_fix": False,
        "clip_skip": 1,
        "control_type": None,
        "image_is_control": False,
        "return_control_map": False,
        "prompt": "an ancient llamia monster",
        "ddim_steps": 15,
        "n_iter": 1,
        "model": model_name,
    }
    pil_image = horde.basic_inference(data)
    if not pil_image:
        logger.error("Inference is failing to generate images")


def do_background_inference():
    """Keep doing inference using random loaded models. To be run in a background thread."""
    count = 1
    while True:
        model = random.choice(SharedModelManager.manager.get_loaded_models_names())
        logger.info(f"Doing inference iteraton {count} with model {model}")
        do_inference(model)
        count += 1


def main():
    horde = HordeLib()
    gpu = GPUInfo()
    SharedModelManager.loadModelManagers(compvis=True)

    report_ram()

    # Reserve 50% of our ram
    UserSettings.ram_to_leave_free_mb = "50%"
    logger.warning(f"Keep {UserSettings.ram_to_leave_free_mb} MB RAM free")

    # Reserve 50% of our vram
    UserSettings.vram_to_leave_free_mb = "50%"
    logger.warning(f"Keep {UserSettings.vram_to_leave_free_mb} MB VRAM free")

    # Get to our limits by loading models
    models = get_available_models()
    model_index = 0
    while True:
        # First we fill ram
        logger.warning("RAM available. Filling RAM")
        while get_free_ram() > UserSettings.ram_to_leave_free_mb:
            add_model(models[model_index])
            model_index += 1
        # Move models into VRAM until we reach our limit
        logger.warning("Filled RAM, now filling VRAM by moving from RAM to VRAM")
        index = 0
        while get_free_vram() > UserSettings.vram_to_leave_free_mb:
            # Move to GPU by using the model
            do_inference(SharedModelManager.manager.get_loaded_models_names()[index])
            index += 1
            if index >= len(SharedModelManager.manager.loaded_models):
                # Maybe our vram is larger than our ram
                break
        logger.warning("Filled VRAM")
        report_ram()
        if get_free_ram() <= UserSettings.ram_to_leave_free_mb and get_free_vram() <= UserSettings.vram_to_leave_free_mb:
            logger.warning("Filled RAM and VRAM")
            break
    
    # From this point, any model loading will push us past our configured resource limits

    # Start doing background inference
    thread = threading.Thread(daemon=True, target=do_background_inference)
    thread.start()

    # Push us past our limits
    add_model(models[model_index])
    model_index += 1
    # That would have pushed something to disk, force a memory cleanup
    cleanup()
    report_ram()

    # Keep loading models whilst doing inference, ram and vram should remain stable
    for i in range(20):
        add_model(models[model_index])
        model_index += 1

if __name__ == "__main__":
    main()
