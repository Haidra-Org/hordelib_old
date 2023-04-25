from hordelib.settings import UserSettings, _UserSettings


class TestWorkerSettings:
    def test_worker_settings_singleton(self):
        a = UserSettings
        b = _UserSettings()
        assert a is b
