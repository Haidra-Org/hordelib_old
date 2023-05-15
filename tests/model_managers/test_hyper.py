# test_horde.py
import pytest
from PIL import Image

from hordelib.horde import HordeLib
from hordelib.shared_model_manager import SharedModelManager


class TestHyperMM:
    @pytest.fixture(autouse=True, scope="class")
    def setup_and_teardown(self):
        TestHyperMM.horde = HordeLib()

        SharedModelManager.loadModelManagers(
            compvis=True,
            blip=True,
            clip=True,
            safety_checker=True,
            esrgan=True,
        )
        assert SharedModelManager.manager is not None
        SharedModelManager.manager.load("RealESRGAN_x4plus")
        SharedModelManager.manager.load("Deliberate")
        SharedModelManager.manager.load("safety_checker")
        yield
        del TestHyperMM.horde
        SharedModelManager._instance = None
        SharedModelManager.manager = None

    def test_get_loaded_models_names(self):
        assert "RealESRGAN_x4plus" in SharedModelManager.manager.get_loaded_models_names()
        assert "Deliberate" in SharedModelManager.manager.get_loaded_models_names()
        assert "safety_checker" in SharedModelManager.manager.get_loaded_models_names()
        assert "Deliberate" in SharedModelManager.manager.get_loaded_models_names(mm_include=["compvis"])
        assert "RealESRGAN_x4plus" not in SharedModelManager.manager.get_loaded_models_names(mm_include=["compvis"])
        assert "safety_checker" not in SharedModelManager.manager.get_loaded_models_names(mm_include=["compvis"])
        assert "Deliberate" in SharedModelManager.manager.get_loaded_models_names(
            mm_include=["compvis", "safety_checker"],
        )
        assert "RealESRGAN_x4plus" not in SharedModelManager.manager.get_loaded_models_names(
            mm_include=["compvis", "safety_checker"],
        )
        assert "safety_checker" in SharedModelManager.manager.get_loaded_models_names(
            mm_include=["compvis", "safety_checker"],
        )
        assert "Deliberate" in SharedModelManager.manager.get_loaded_models_names(mm_exclude=["esrgan"])
        assert "RealESRGAN_x4plus" not in SharedModelManager.manager.get_loaded_models_names(mm_exclude=["esrgan"])
        assert "safety_checker" in SharedModelManager.manager.get_loaded_models_names(mm_exclude=["esrgan"])

    def test_get_available_models_by_types(self):
        assert "RealESRGAN_x4plus" in SharedModelManager.manager.get_available_models_by_types()
        assert "Deliberate" in SharedModelManager.manager.get_available_models_by_types()
        assert "safety_checker" in SharedModelManager.manager.get_available_models_by_types()
        assert "Deliberate" in SharedModelManager.manager.get_available_models_by_types(mm_include=["compvis"])
        assert "RealESRGAN_x4plus" not in SharedModelManager.manager.get_available_models_by_types(
            mm_include=["compvis"],
        )
        assert "safety_checker" not in SharedModelManager.manager.get_available_models_by_types(mm_include=["compvis"])
        assert "Deliberate" in SharedModelManager.manager.get_available_models_by_types(
            mm_include=["compvis", "safety_checker"],
        )
        assert "RealESRGAN_x4plus" not in SharedModelManager.manager.get_available_models_by_types(
            mm_include=["compvis", "safety_checker"],
        )
        assert "safety_checker" in SharedModelManager.manager.get_available_models_by_types(
            mm_include=["compvis", "safety_checker"],
        )
        assert "Deliberate" in SharedModelManager.manager.get_available_models_by_types(mm_exclude=["esrgan"])
        assert "RealESRGAN_x4plus" not in SharedModelManager.manager.get_available_models_by_types(
            mm_exclude=["esrgan"],
        )
        assert "safety_checker" in SharedModelManager.manager.get_available_models_by_types(mm_exclude=["esrgan"])
