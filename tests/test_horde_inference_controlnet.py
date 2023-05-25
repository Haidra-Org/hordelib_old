# test_horde.py
import os

import pytest
from PIL import Image

from hordelib.horde import HordeLib
from hordelib.shared_model_manager import SharedModelManager
from hordelib.utils.distance import are_images_identical


class TestHordeInference:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.horde = HordeLib()

        self.default_model_manager_args = {
            # aitemplate
            # "blip": True,
            # "clip": True,
            # "codeformer": True,
            "compvis": True,
            "controlnet": True,
            # "diffusers": True,
            # "esrgan": True,
            # "gfpgan": True,
            # "safety_checker": True,
        }
        SharedModelManager.loadModelManagers(**self.default_model_manager_args)
        assert SharedModelManager.manager is not None
        SharedModelManager.manager.load("Deliberate")
        for preproc in HordeLib.CONTROLNET_IMAGE_PREPROCESSOR_MAP.keys():
            SharedModelManager.manager.controlnet.download_control_type(preproc, ["stable diffusion 1"])
        TestHordeInference.distance_threshold = int(os.getenv("IMAGE_DISTANCE_THRESHOLD", "100000"))
        yield
        del self.horde
        SharedModelManager._instance = None
        SharedModelManager.manager = None

    def test_controlnet_sd1(self):
        data = {
            "sampler_name": "k_dpmpp_2m",
            "cfg_scale": 7.5,
            "denoising_strength": 1.0,
            "seed": 123456789,
            "height": 512,
            "width": 512,
            "karras": False,
            "tiling": False,
            "hires_fix": False,
            "clip_skip": 1,
            "control_type": "",
            "image_is_control": False,
            "return_control_map": False,
            "prompt": "a man walking in the snow",
            "ddim_steps": 25,
            "n_iter": 1,
            "model": "Deliberate",
            "source_image": Image.open("images/test_db0.jpg"),
            "source_processing": "img2img",
        }
        assert self.horde is not None
        for preproc in HordeLib.CONTROLNET_IMAGE_PREPROCESSOR_MAP.keys():
            if preproc == "scribble" or preproc == "mlsd":
                # Skip
                continue
            assert (
                SharedModelManager.manager.controlnet.check_control_type_available(
                    preproc,
                    "stable diffusion 1",
                )
                is True
            )
            data["control_type"] = preproc
            pil_image = self.horde.basic_inference(data)
            assert pil_image is not None
            # assert get_image_distance(expected_filename, pil_image) < 100
            img_filename = f"controlnet_{preproc}.png"
            pil_image.save(f"images/{img_filename}", quality=100)
            assert are_images_identical(f"images_expected/{img_filename}", pil_image, self.distance_threshold)

    def test_controlnet_fake_cn(self):
        data = {
            "sampler_name": "k_dpmpp_2m",
            "cfg_scale": 7.5,
            "denoising_strength": 1.0,
            "seed": 123456789,
            "height": 512,
            "width": 512,
            "karras": False,
            "tiling": False,
            "hires_fix": False,
            "clip_skip": 1,
            "control_type": "THIS_SHOULD_FAIL",
            "image_is_control": False,
            "return_control_map": False,
            "prompt": "a man walking in the snow",
            "ddim_steps": 25,
            "n_iter": 1,
            "model": "Deliberate",
            "source_image": Image.open("images/test_db0.jpg"),
            "source_processing": "img2img",
        }
        assert self.horde is not None
        with pytest.raises(Exception):
            pil_image = self.horde.basic_inference(data)
            assert pil_image is None

    def test_controlnet_strength(self):
        data = {
            "sampler_name": "k_dpmpp_2m",
            "cfg_scale": 7.5,
            "denoising_strength": 1.0,
            "seed": 123456789,
            "height": 512,
            "width": 512,
            "karras": False,
            "tiling": False,
            "hires_fix": False,
            "clip_skip": 1,
            "control_type": "canny",
            "image_is_control": False,
            "return_control_map": False,
            "prompt": "a man walking on the moon",
            "ddim_steps": 25,
            "n_iter": 1,
            "model": "Deliberate",
            "source_image": Image.open("images/test_db0.jpg"),
            "source_processing": "img2img",
        }
        for strength in [1.0, 0.5, 0.2]:
            data["control_strength"] = strength
            pil_image = self.horde.basic_inference(data)
            assert pil_image is not None
            img_filename = f"controlnet_strength_{strength}.png"
            pil_image.save(f"images/{img_filename}", quality=100)
            assert are_images_identical(f"images_expected/{img_filename}", pil_image, self.distance_threshold)

    def test_controlnet_hires_fix(self):
        data = {
            "sampler_name": "k_dpmpp_2m",
            "cfg_scale": 7.5,
            "denoising_strength": 1.0,
            "seed": 1234345378856789,
            "height": 768,
            "width": 768,
            "karras": False,
            "tiling": False,
            "hires_fix": True,
            "hires_fix_denoising_strength": 0.0,
            "clip_skip": 1,
            "control_type": "canny",
            "image_is_control": False,
            "return_control_map": False,
            "prompt": "a man walking in the jungle",
            "ddim_steps": 15,
            "n_iter": 1,
            "model": "Deliberate",
            "source_image": Image.open("images/test_db0.jpg"),
            "source_processing": "img2img",
        }
        for denoise in [0.4, 0.5, 0.6]:
            data["hires_fix_denoising_strength"] = denoise
            pil_image = self.horde.basic_inference(data)
            assert pil_image is not None
            img_filename = f"controlnet_hires_fix_denoise_{denoise}.png"
            pil_image.save(f"images/{img_filename}", quality=100)
            assert are_images_identical(f"images_expected/{img_filename}", pil_image, self.distance_threshold)
