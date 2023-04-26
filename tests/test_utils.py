from hordelib.settings import UserSettings


class TestWorkerSettings:
    def test_worker_settings_singleton(self):
        a = UserSettings._instance
        assert a is not None
        b = UserSettings()
        assert b._instance is not None
        assert a is b._instance
