# consts.py
from enum import Enum, auto

# hordelib version
VERSION = "v0.4.1"
"""The version of the hordelib library."""

COMFYUI_VERSION = "c767e9426ae81bed4f52c7be0625f0efc4cbe16b"
"""The exact version of ComfyUI version to load."""

REMOTE_MODEL_DB = (
    "https://raw.githubusercontent.com/db0/AI-Horde-image-model-reference/main/"
)
"""The default base endpoint where to find model databases. See MODEL_DB_NAMES for valid database names."""


class HordeSupportedBackends(Enum):
    ComfyUI = auto()


class ModelCategoryNames(str, Enum):
    """Look up str enum for the categories of models (compvis, controlnet, clip, etc...)."""

    blip = "blip"
    clip = "clip"
    codeformer = "codeformer"
    compvis = "compvis"
    controlnet = "controlnet"
    diffusers = "diffusers"
    esrgan = "esrgan"
    gfpgan = "gfpgan"
    safety_checker = "safety_checker"


# Default model managers to load
DEFAULT_MODEL_MANAGERS = {
    ModelCategoryNames.blip: True,
    ModelCategoryNames.clip: True,
    ModelCategoryNames.codeformer: True,
    ModelCategoryNames.compvis: True,
    ModelCategoryNames.controlnet: True,
    ModelCategoryNames.diffusers: True,
    ModelCategoryNames.esrgan: True,
    ModelCategoryNames.gfpgan: True,
    ModelCategoryNames.safety_checker: True,
}
"""The default model managers to load."""  # XXX Clarify

MODEL_DB_NAMES = {
    ModelCategoryNames.blip: ModelCategoryNames.blip,
    ModelCategoryNames.clip: ModelCategoryNames.clip,
    ModelCategoryNames.codeformer: ModelCategoryNames.codeformer,
    ModelCategoryNames.compvis: "stable_diffusion",
    ModelCategoryNames.controlnet: ModelCategoryNames.controlnet,
    ModelCategoryNames.diffusers: ModelCategoryNames.diffusers,
    ModelCategoryNames.esrgan: ModelCategoryNames.esrgan,
    ModelCategoryNames.gfpgan: ModelCategoryNames.gfpgan,
    ModelCategoryNames.safety_checker: ModelCategoryNames.safety_checker,
}
"""The name of the json file (without the extension) of the corresponding model database."""

MODEL_FOLDER_NAMES = {
    ModelCategoryNames.blip: ModelCategoryNames.blip,
    ModelCategoryNames.clip: ModelCategoryNames.clip,
    ModelCategoryNames.codeformer: ModelCategoryNames.codeformer,
    ModelCategoryNames.compvis: "compvis",
    ModelCategoryNames.controlnet: ModelCategoryNames.controlnet,
    ModelCategoryNames.diffusers: ModelCategoryNames.diffusers,
    ModelCategoryNames.esrgan: ModelCategoryNames.esrgan,
    ModelCategoryNames.gfpgan: ModelCategoryNames.gfpgan,
    ModelCategoryNames.safety_checker: ModelCategoryNames.safety_checker,
}
"""The folder name on disk where the models are stored in AIWORKER_CACHE_HOME."""
