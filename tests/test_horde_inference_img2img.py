# test_horde.py
import os

import pytest
from PIL import Image

from hordelib.horde import HordeLib
from hordelib.shared_model_manager import SharedModelManager
from hordelib.utils.distance import are_images_identical


class TestHordeInference:
    @pytest.fixture(autouse=True, scope="class")
    def setup_and_teardown(self):
        TestHordeInference.horde = HordeLib()

        TestHordeInference.default_model_manager_args = {
            # aitemplate
            # "blip": True,
            # "clip": True,
            # "codeformer": True,
            "compvis": True,
            # "controlnet": True,
            # "diffusers": True,
            # "esrgan": True,
            # "gfpgan": True,
            # "safety_checker": True,
        }
        SharedModelManager.loadModelManagers(**self.default_model_manager_args)
        assert SharedModelManager.manager is not None
        SharedModelManager.manager.load("Deliberate")
        TestHordeInference.distance_threshold = int(os.getenv("IMAGE_DISTANCE_THRESHOLD", "100000"))
        yield
        del TestHordeInference.horde
        SharedModelManager._instance = None
        SharedModelManager.manager = None

    def test_image_to_image(self):
        data = {
            "sampler_name": "k_dpmpp_2m",
            "cfg_scale": 7.5,
            "denoising_strength": 0.4,
            "seed": 666,
            "height": 512,
            "width": 512,
            "karras": False,
            "tiling": False,
            "hires_fix": False,
            "clip_skip": 1,
            "control_type": None,
            "image_is_control": False,
            "return_control_map": False,
            "prompt": "a dinosaur",
            "ddim_steps": 25,
            "n_iter": 1,
            "model": "Deliberate",
            "source_image": Image.open("images/test_db0.jpg"),
            "source_processing": "img2img",
        }
        assert self.horde is not None
        pil_image = self.horde.basic_inference(data)
        assert pil_image is not None
        assert pil_image.size == (512, 512)
        img_filename = "image_to_image.png"
        pil_image.save(f"images/{img_filename}", quality=100)
        assert are_images_identical(f"images_expected/{img_filename}", pil_image, self.distance_threshold)

    def test_image_to_image_hires_fix_small(self):
        data = {
            "sampler_name": "k_dpmpp_2m",
            "cfg_scale": 7.5,
            "denoising_strength": 0.4,
            "seed": 666,
            "height": 512,
            "width": 512,
            "karras": False,
            "tiling": False,
            "hires_fix": True,
            "clip_skip": 1,
            "control_type": None,
            "image_is_control": False,
            "return_control_map": False,
            "prompt": "a dinosaur",
            "ddim_steps": 25,
            "n_iter": 1,
            "model": "Deliberate",
            "source_image": Image.open("images/test_db0.jpg"),
            "source_processing": "img2img",
        }
        assert self.horde is not None
        pil_image = self.horde.basic_inference(data)
        assert pil_image is not None
        assert pil_image.size == (512, 512)
        img_filename = "image_to_image_hires_fix_small.png"
        pil_image.save(f"images/{img_filename}", quality=100)
        assert are_images_identical(f"images_expected/{img_filename}", pil_image, self.distance_threshold)

    def test_image_to_image_hires_fix_large(self):
        data = {
            "sampler_name": "k_dpmpp_2m",
            "cfg_scale": 7.5,
            "denoising_strength": 0.4,
            "seed": 1312,
            "height": 768,
            "width": 768,
            "karras": False,
            "tiling": False,
            "hires_fix": True,
            "clip_skip": 1,
            "control_type": None,
            "image_is_control": False,
            "return_control_map": False,
            "prompt": "a dinosaur",
            "ddim_steps": 25,
            "n_iter": 1,
            "model": "Deliberate",
            "source_image": Image.open("images/test_db0.jpg"),
            "source_processing": "img2img",
        }
        assert self.horde is not None
        pil_image = self.horde.basic_inference(data)
        assert pil_image is not None
        assert pil_image.size == (768, 768)
        img_filename = "image_to_image_hires_fix_large.png"
        pil_image.save(f"images/{img_filename}", quality=100)
        assert are_images_identical(f"images_expected/{img_filename}", pil_image, self.distance_threshold)

    def test_img2img_masked_denoise_1(self):
        data = {
            "sampler_name": "k_dpmpp_2m",
            "cfg_scale": 7.5,
            "denoising_strength": 1,
            "seed": 24636666,
            "height": 512,
            "width": 512,
            "karras": False,
            "clip_skip": 1,
            "prompt": "a mecha robot sitting on a bench",
            "ddim_steps": 20,
            "n_iter": 1,
            "model": "Deliberate",
            "source_image": Image.open("images/test_img2img_alpha.png"),
            "source_processing": "img2img",
        }
        assert self.horde is not None
        pil_image = self.horde.basic_inference(data)
        assert pil_image is not None
        assert pil_image.size == (512, 512)
        img_filename = "img2img_to_masked_denoise_1.png"
        pil_image.save(f"images/{img_filename}", quality=100)
        assert are_images_identical(f"images_expected/{img_filename}", pil_image, self.distance_threshold)

    def test_img2img_masked_denoise_high(self):
        data = {
            "sampler_name": "k_dpmpp_2m",
            "cfg_scale": 7.5,
            "denoising_strength": 0.6,
            "seed": 3,
            "height": 512,
            "width": 512,
            "karras": False,
            "clip_skip": 1,
            "prompt": "a mecha robot sitting on a bench",
            "ddim_steps": 20,
            "n_iter": 1,
            "model": "Deliberate",
            "source_image": Image.open("images/test_img2img_alpha.png"),
            "source_processing": "img2img",
        }
        assert self.horde is not None
        pil_image = self.horde.basic_inference(data)
        assert pil_image is not None
        assert pil_image.size == (512, 512)
        img_filename = "img2img_to_masked_denoise_0.6.png"
        pil_image.save(f"images/{img_filename}", quality=100)
        assert are_images_identical(f"images_expected/{img_filename}", pil_image, self.distance_threshold)

    def test_img2img_masked_denoise_mid(self):
        data = {
            "sampler_name": "k_dpmpp_2m",
            "cfg_scale": 7.5,
            "denoising_strength": 0.4,
            "seed": 3,
            "height": 512,
            "width": 512,
            "karras": False,
            "clip_skip": 1,
            "prompt": "a mecha robot sitting on a bench",
            "ddim_steps": 20,
            "n_iter": 1,
            "model": "Deliberate",
            "source_image": Image.open("images/test_img2img_alpha.png"),
            "source_processing": "img2img",
        }
        assert self.horde is not None
        pil_image = self.horde.basic_inference(data)
        assert pil_image is not None
        assert pil_image.size == (512, 512)
        img_filename = "img2img_to_masked_denoise_0.4.png"
        pil_image.save(f"images/{img_filename}", quality=100)
        assert are_images_identical(f"images_expected/{img_filename}", pil_image, self.distance_threshold)

    def test_img2img_masked_denoise_low(self):
        data = {
            "sampler_name": "k_dpmpp_2m",
            "cfg_scale": 7.5,
            "denoising_strength": 0.2,
            "seed": 3,
            "height": 512,
            "width": 512,
            "karras": False,
            "clip_skip": 1,
            "prompt": "a mecha robot sitting on a bench",
            "ddim_steps": 20,
            "n_iter": 1,
            "model": "Deliberate",
            "source_image": Image.open("images/test_img2img_alpha.png"),
            "source_processing": "img2img",
        }
        assert self.horde is not None
        pil_image = self.horde.basic_inference(data)
        assert pil_image is not None
        assert pil_image.size == (512, 512)
        img_filename = "img2img_to_masked_denoise_0.2.png"
        pil_image.save(f"images/{img_filename}", quality=100)
        assert are_images_identical(f"images_expected/{img_filename}", pil_image, self.distance_threshold)

    def test_image_to_faulty_source_image(self):
        data = {
            "sampler_name": "k_dpmpp_2m",
            "cfg_scale": 7.5,
            "denoising_strength": 1.0,
            "seed": 123456789,
            "height": 512.1,  # test param fix
            "width": 512.1,  # test param fix
            "karras": False,
            "tiling": False,
            "hires_fix": False,
            "clip_skip": 1,
            "control_type": None,
            "image_is_control": False,
            "return_control_map": False,
            "prompt": "an ancient llamia monster",
            "ddim_steps": 25,
            "n_iter": 1,
            "model": "Deliberate",
            "source_image": "THIS SHOULD FAILOVER TO TEXT2IMG",
            "source_processing": "img2img",
        }
        assert self.horde is not None
        pil_image = self.horde.basic_inference(data)
        assert pil_image is not None
        img_filename = "img2img_fallback_to_txt2img.png"
        pil_image.save(f"images/{img_filename}", quality=100)
        assert are_images_identical(f"images_expected/{img_filename}", pil_image, self.distance_threshold)
