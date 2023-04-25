import re

import psutil
from typing_extensions import Self

from hordelib.utils.gpuinfo import GPUInfo
from hordelib.utils.switch import Switch


class _UserSettings:
    """Container class for all user settings."""

    _instance: Self | None = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        # Default to 50% resource usage
        self.vram_to_leave_free_mb = "50%"
        self.ram_to_leave_free_mb = "50%"

    def _is_percentage(self, value):
        if isinstance(value, str):
            if re.match(r"^\d+(\.\d+)?%$", value):
                return float(value.strip("%"))
        return False

    def _get_total_vram_mb(self):
        try:
            gpu = GPUInfo()
            return gpu.get_total_vram_mb()
        except Exception:
            return 0

    def _get_total_ram_mb(self):
        virtual_memory = psutil.virtual_memory()
        return virtual_memory.total / (1024 * 1024)

    # Hordelib will try to leave at least this much VRAM free
    @property
    def vram_to_leave_free_mb(self):
        return self._vram_to_leave_free_mb

    @vram_to_leave_free_mb.setter
    def vram_to_leave_free_mb(self, value):
        # Allow this to be expressed as a number (in MB) or a percentage
        if perc := self._is_percentage(value):
            value = int((perc / 100) * self._get_total_vram_mb())
        else:
            try:
                value = int(value)
            except ValueError:
                value = 0
        self._vram_to_leave_free_mb = value

    # Hordelib will try to leave at least this much system RAM free
    @property
    def ram_to_leave_free_mb(self):
        return self._ram_to_leave_free_mb

    @ram_to_leave_free_mb.setter
    def ram_to_leave_free_mb(self, value):
        # Allow this to be expressed as a number (in MB) or a percentage
        if perc := self._is_percentage(value):
            value = int((perc / 100) * self._get_total_ram_mb())
        else:
            try:
                value = int(value)
            except ValueError:
                value = 0
        self._ram_to_leave_free_mb = value

    # Disable the use of xformers
    disable_xformers = Switch()

    # Disable the display of progress bars when downloading
    # FIXME We should enable these, but don't yet
    disable_download_progress = Switch()

    # Disable disk caching completely
    disable_disk_cache = Switch()


UserSettings = _UserSettings()
