# This tests running hordelib standalone, as an external caller would use it.
# Call with: python -m test.run_memory_test
# You need all the deps in whatever environment you are running this.
import psutil
from loguru import logger

import hordelib
hordelib.initialise(setup_logging=False)

from hordelib.horde import HordeLib
from hordelib.shared_model_manager import SharedModelManager
from hordelib.settings import UserSettings
from hordelib.utils.gpuinfo import GPUInfo


def get_ram():
    virtual_memory = psutil.virtual_memory()
    total_ram_mb = virtual_memory.total / (1024 * 1024)
    used_ram = virtual_memory.used / (1024 * 1024)
    free_ram = total_ram_mb - used_ram
    return (int(total_ram_mb), int(used_ram), int(free_ram))


def report_ram():
    gpu = GPUInfo()
    total, used, free = get_ram()
    logger.warning(f"Free RAM {free} MB")
    logger.warning(f"Free VRAM {gpu.get_free_vram_mb()} MB")


def add_model(model_name):
    SharedModelManager.manager.load(model_name)
    report_ram()


def get_available_models():
    models = SharedModelManager.manager.get_available_models()
    return models


def main():
    horde = HordeLib()
    gpu = GPUInfo()
    SharedModelManager.loadModelManagers(compvis=True)

    report_ram()
    total, used, free = get_ram()

    # Reserve 50% of our ram
    UserSettings.ram_to_leave_free_mb = "50%"
    logger.warning(f"Keep {UserSettings.ram_to_leave_free_mb} MB RAM free")

    # Reserve 50% of our vram
    UserSettings.vram_to_leave_free_mb = "50%"
    logger.warning(f"Keep {UserSettings.vram_to_leave_free_mb} MB VRAM free")


if __name__ == "__main__":
    main()
