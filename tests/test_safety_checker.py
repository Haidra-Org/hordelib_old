# test_horde.py
import pytest
import numpy as np
from PIL import Image

from hordelib.horde import HordeLib
from hordelib.shared_model_manager import SharedModelManager
from transformers import CLIPFeatureExtractor


class TestHordePostProcessing:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.horde = HordeLib()

        self.default_model_manager_args = {
            # aitemplate
            # "blip": True,
            # "clip": True,
            # "codeformer": True,
            # "compvis": True,
            # "controlnet": True,
            # "diffusers": True,
            # "esrgan": True,
            # "gfpgan": True,
            "safety_checker": True,
        }
        self.image = Image.open("db0.jpg") 
        SharedModelManager.loadModelManagers(**self.default_model_manager_args)
        assert SharedModelManager.manager is not None
        SharedModelManager.manager.load("safety_checker")
        yield
        del self.horde
        SharedModelManager._instance = None
        SharedModelManager.manager = None

    def test_load(self):
        assert SharedModelManager.manager.safety_checker.is_model_loaded("safety_checker") is True

    def test_safety_checker(self):
        safety_checker = SharedModelManager.manager.loaded_models["safety_checker"]["model"]
        feature_extractor = CLIPFeatureExtractor()
        image_features = feature_extractor(self.image, return_tensors="pt").to("cpu")
        _, has_nsfw_concept = safety_checker(
            clip_input=image_features.pixel_values,
            images=[np.asarray(self.image)],
        )
        assert has_nsfw_concept is not None
        assert False in has_nsfw_concept
