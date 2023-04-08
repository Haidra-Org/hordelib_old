# This tests running hordelib standalone, as an external caller would use it.
# Call with: python -m test.run_txt2img
# You need all the deps in whatever environment you are running this.
import os

import hordelib

hordelib.initialise()

from hordelib.horde import HordeLib
from hordelib.shared_model_manager import SharedModelManager

generate = HordeLib()
SharedModelManager.loadModelManagers(compvis=True)
SharedModelManager.manager.load("Deliberate")

data = {
    "sampler_name": "k_dpmpp_2m",
    "cfg_scale": 7.5,
    "denoising_strength": 1.0,
    "seed": 123456789,
    "height": 512,
    "width": 512,
    "karras": True,
    "tiling": False,
    "hires_fix": False,
    "clip_skip": 1,
    "control_type": "canny",
    "image_is_control": False,
    "return_control_map": False,
    "prompt": "an ancient llamia monster",
    "ddim_steps": 25,
    "n_iter": 1,
    "model": "Deliberate",
}
pil_image = generate.text_to_image(data)
pil_image.save("images/test.png")
