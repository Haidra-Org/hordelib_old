# This tests running hordelib standalone, as an external caller would use it.
# Call with: python -m test.run_txt2img
# You need all the deps in whatever environment you are running this.
import os

from loguru import logger

import hordelib


def main():
    hordelib.initialise(setup_logging=False)

    from hordelib.horde import HordeLib
    from hordelib.shared_model_manager import SharedModelManager

    HordeLib()
    SharedModelManager.loadModelManagers(lora=True)
    SharedModelManager.manager.lora.download_default_loras()
    SharedModelManager.manager.lora.wait_for_downloads(30)
    logger.info(SharedModelManager.manager.lora.get_available_models())


if __name__ == "__main__":
    main()
