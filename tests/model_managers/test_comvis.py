import pytest

import hordelib


class TestCompvis:
    _initialised = False

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        if not self._initialised:
            hordelib.initialise()
        from hordelib.model_manager.compvis import CompVisModelManager

        self.compvis_model_manager = CompVisModelManager()
        assert self.compvis_model_manager is not None
        yield
        del self.compvis_model_manager

    def test_safety_checker_load_defaults(self):
        success = self.compvis_model_manager.load("Deliberate")
        assert success
