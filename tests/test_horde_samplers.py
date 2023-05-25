# test_horde.py
import os

import pytest
from PIL import Image

from hordelib.horde import HordeLib
from hordelib.shared_model_manager import SharedModelManager
from hordelib.utils.distance import are_images_identical

SLOW_SAMPLERS = ["k_dpmpp_2s_a", "k_dpmpp_sde", "k_heun", "k_dpm_2", "k_dpm_2_a"]


class TestHordeSamplers:
    @pytest.fixture(autouse=True, scope="class")
    def setup_and_teardown(self):
        TestHordeSamplers.horde = HordeLib()

        SharedModelManager.loadModelManagers(compvis=True)
        assert SharedModelManager.manager is not None
        SharedModelManager.manager.load("Deliberate")
        TestHordeSamplers.distance_threshold = int(os.getenv("IMAGE_DISTANCE_THRESHOLD", "100000"))
        yield
        del TestHordeSamplers.horde
        SharedModelManager._instance = None
        SharedModelManager.manager = None

    def test_samplers(self):
        data = {
            "sampler_name": "",
            "cfg_scale": 6.5,
            "denoising_strength": 1.0,
            "seed": 3688490319,
            "height": 512,
            "width": 512,
            "karras": False,
            "tiling": False,
            "hires_fix": False,
            "clip_skip": 1,
            "control_type": None,
            "image_is_control": False,
            "return_control_map": False,
            "prompt": (
                "a woman closeup made out of metal, (cyborg:1.1), realistic skin, (detailed wire:1.3), "
                "(intricate details), hdr, (intricate details, hyperdetailed:1.2), cinematic shot, "
                "vignette, centered"
            ),
            "ddim_steps": 30,
            "n_iter": 1,
            "model": "Deliberate",
        }
        assert self.horde is not None
        for sampler in HordeLib.SAMPLERS_MAP.keys():
            data["sampler_name"] = sampler.upper()  # force uppercase to ensure case insensitive
            pil_image = self.horde.basic_inference(data)
            assert pil_image is not None
            img_filename = f"sampler_30_steps_{sampler}.png"
            pil_image.save(f"images/{img_filename}", quality=100)
            assert are_images_identical(f"images_expected/{img_filename}", pil_image, self.distance_threshold)

    def test_slow_samplers(self):
        data = {
            "sampler_name": "",
            "cfg_scale": 6.5,
            "denoising_strength": 1.0,
            "seed": 3688390309,
            "height": 512,
            "width": 512,
            "karras": False,
            "tiling": False,
            "hires_fix": False,
            "clip_skip": 1,
            "control_type": None,
            "image_is_control": False,
            "return_control_map": False,
            "prompt": (
                "an old man closeup, (hr giger:1.1), (detailed wire:1.3), "
                "(intricate details), hdr, (intricate details, hyperdetailed:1.2), cinematic shot, "
                "vignette, centered"
            ),
            "ddim_steps": 10,
            "n_iter": 1,
            "model": "Deliberate",
        }
        assert self.horde is not None
        for sampler in SLOW_SAMPLERS:
            data["sampler_name"] = sampler
            pil_image = self.horde.basic_inference(data)
            assert pil_image is not None
            img_filename = f"sampler_10_steps_{sampler}.png"
            pil_image.save(f"images/{img_filename}", quality=100)
            assert are_images_identical(f"images_expected/{img_filename}", pil_image, self.distance_threshold)
