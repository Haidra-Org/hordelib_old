# test_utils.py


class TestWorkerSettings:
    def test_checkSwitch(self):
        from hordelib.settings import WorkerSettings
        from hordelib.utils import switch

        assert isinstance(WorkerSettings.disable_download_progress, switch.Switch)

        WorkerSettings.disable_download_progress.activate()
        assert WorkerSettings.disable_download_progress.active is True
        WorkerSettings.disable_download_progress.disable()
        assert WorkerSettings.disable_download_progress.active is False
        WorkerSettings.disable_download_progress.toggle(True)
        assert WorkerSettings.disable_download_progress.active is True
