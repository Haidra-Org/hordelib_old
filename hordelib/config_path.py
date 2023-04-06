import os
import sys


def get_hordelib_path() -> str:
    """Returns the path hordelib is installed in."""
    current_file_path = os.path.abspath(__file__)
    return os.path.dirname(current_file_path)


def get_comfyui_path() -> str:
    """Returns the path to ComfyUI that hordelib installs and manages."""
    return os.path.join(get_hordelib_path(), "ComfyUI")


def set_system_path() -> None:
    """Adds ComfyUI to the python path, as it is not a proper library."""
    sys.path.append(get_comfyui_path())


def is_comfy_path_set() -> bool:
    return get_comfyui_path() in sys.path
