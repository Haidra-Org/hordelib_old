# test_horde.py
import pytest

from hordelib.horde import HordeLib
from hordelib.shared_model_manager import SharedModelManager


class TestSharedModelManager:
    horde = HordeLib()
    default_model_manager_args: dict

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.horde = HordeLib()

        self.default_model_manager_args = {  # XXX # FIXME
            # aitemplate
            "blip": False,
            "clip": True,
            "codeformer": False,
            "compvis": True,
            "controlnet": False,
            "diffusers": True,
            "esrgan": False,
            "gfpgan": False,
            "safety_checker": False,  # XXX
        }
        SharedModelManager.loadModelManagers(**self.default_model_manager_args)
        assert SharedModelManager.manager is not None
        yield
        del self.horde
        SharedModelManager._instance = None
        SharedModelManager.manager = None

    def test_diffusers(self):
        from hordelib.model_manager.diffusers import DiffusersModelManager

        difusersMM = DiffusersModelManager()
        difusersMM.load("stable_diffusion_inpainting")
        pass

    def test_compvis(self):
        from hordelib.model_manager.compvis import CompVisModelManager

        CompVisModelManager()

    def test_singleton(self):
        a = SharedModelManager()
        b = SharedModelManager()
        assert a.manager is b.manager

    def test_horde_model_manager_init(self):
        assert SharedModelManager.manager is not None
        # assert SharedModelManager.manager.aitemplate is not None
        assert SharedModelManager.manager.blip is not None
        assert SharedModelManager.manager.clip is not None
        assert SharedModelManager.manager.codeformer is not None
        assert SharedModelManager.manager.compvis is not None
        assert SharedModelManager.manager.controlnet is not None
        assert SharedModelManager.manager.diffusers is not None
        assert SharedModelManager.manager.esrgan is not None
        assert SharedModelManager.manager.gfpgan is not None
        assert SharedModelManager.manager.safety_checker is not None

    def test_horde_model_manager_reload_db(self):
        assert SharedModelManager.manager is not None
        SharedModelManager.manager.reload_database()

    def test_horde_model_manager_download_model(self):
        assert SharedModelManager.manager is not None
        result: bool | None = SharedModelManager.manager.download_model("Deliberate")
        assert result is True

    def test_horde_model_manager_validate(self):
        assert SharedModelManager.manager is not None
        SharedModelManager.manager.load("Deliberate")
        result: bool | None = SharedModelManager.manager.validate_model("Deliberate")
        assert result is True

    def test_taint_models(self):
        assert SharedModelManager.manager is not None
        SharedModelManager.manager.taint_models(["Deliberate"])
        assert "Deliberate" not in SharedModelManager.manager.get_available_models()
        assert "Deliberate" not in SharedModelManager.manager.get_loaded_models_names()

    # XXX add a test for model missing?
    def test_horde_model_manager_unload_model(self):
        assert SharedModelManager.manager is not None
        SharedModelManager.manager.load("Deliberate")
        assert "Deliberate" in SharedModelManager.manager.get_loaded_models_names()
        result = SharedModelManager.manager.unload_model("Deliberate")
        assert result is True
        assert "Deliberate" not in SharedModelManager.manager.get_loaded_models_names()
