import os
import sys

from hordelib import install
from hordelib.model_manager.hyper import ModelManager
from hordelib.utils.switch import Switch

VERSION = "0.0.10"
COMFYUI_VERSION = "72f9235a491e7800b3a7686e4901729d371dabed"

current_file_path = os.path.abspath(__file__)
current_folder = os.path.dirname(current_file_path)
comfypath = os.path.join(current_folder, "ComfyUI")
sys.path.append(comfypath)  # noqa: E402

installer = install.Installer()
installer.install(COMFYUI_VERSION)


disable_xformers = Switch()
disable_voodoo = Switch()
enable_local_ray_temp = Switch()
disable_progress = Switch()
disable_download_progress = Switch()
enable_ray_alternative = Switch()

horde_model_manager = None  # This needs


class HordelibException(Exception):
    pass


def set_horde_model_manager(mm: ModelManager):
    global horde_model_manager
    horde_model_manager = mm
