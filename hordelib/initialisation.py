# initialisation.py
# Initialise hordelib.
import sys

from loguru import logger
from hordelib import install_comfy
from hordelib.config_path import set_system_path, get_hordelib_path
from hordelib.consts import COMFYUI_VERSION, DEFAULT_MODEL_MANAGERS, RELEASE_VERSION


def initialise():
    # If developer mode, don't permit some things
    if not RELEASE_VERSION and " " in get_hordelib_path():
        # Our runtime patching can't handle this
        raise Exception(
            "Do not run this project in developer mode from a path that "
            "contains spaces in directory names."
        )

    # Ensure we have ComfyUI
    logger.debug("Clearing command line args in sys.argv before ComfyUI load")
    sys_arg_bkp = sys.argv.copy()
    sys.argv = sys.argv[:1]
    installer = install_comfy.Installer()
    installer.install(COMFYUI_VERSION)

    # Modify python path to include comfyui
    set_system_path()

    # Initialise model manager
    from hordelib.shared_model_manager import SharedModelManager

    SharedModelManager.loadModelManagers(**DEFAULT_MODEL_MANAGERS)
    sys.argv = sys_arg_bkp
