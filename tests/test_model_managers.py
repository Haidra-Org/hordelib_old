import pytest


class TestSafetyChecker:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        import hordelib.model_manager.safety_checker as safety_checker

    def test_safety_checker_init(self):
        safety_model_manager = safety_checker.SafetyCheckerModelManager()

    def test_safety_checker_load_defaults(self):
        safety_model_manager = safety_checker.SafetyCheckerModelManager()
        safety_model_manager.load("safety_checker")

    def test_safety_checker_load_cpu_only(self):
        safety_model_manager = safety_checker.SafetyCheckerModelManager()
        safety_model_manager.load("safety_checker", cpu_only=True)
