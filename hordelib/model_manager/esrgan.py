import time

import torch
from basicsr.archs.rrdbnet_arch import RRDBNet
from loguru import logger
from realesrgan import RealESRGANer
from realesrgan.archs.srvgg_arch import SRVGGNetCompact

from hordelib.cache import get_cache_directory
from hordelib.model_manager.base import BaseModelManager
from hordelib.ComfyUI import comfy, comfy_extras


class EsrganModelManager(BaseModelManager):
    def __init__(self, download_reference=True):
        super().__init__()
        self.download_reference = download_reference
        self.path = f"{get_cache_directory()}/esrgan"
        self.models_db_name = "esrgan"
        self.models_path = self.pkg / f"{self.models_db_name}.json"
        self.remote_db = f"https://raw.githubusercontent.com/db0/AI-Horde-image-model-reference/main/{self.models_db_name}.json"
        self.init()

    def load(
        self,
        model_name: str,
    ):
        """
        model_name: str. Name of the model to load. See available_models for a list of available models.
        """

        # if not self.cuda_available:
        #     cpu_only = True
        if model_name not in self.models:
            logger.error(f"{model_name} not found")
            return False
        if model_name not in self.available_models:
            logger.error(f"{model_name} not available")
            logger.info(
                f"Downloading {model_name}", status="Downloading"
            )  # logger.init_ok
            self.download_model(model_name)
            logger.info(
                f"{model_name} downloaded", status="Downloading"
            )  # logger.init_ok
        if model_name not in self.loaded_models:
            tic = time.time()
            logger.info(f"{model_name}", status="Loading")  # logger.init

            self.loaded_models[model_name] = self.load_esrgan(
                model_name,
            )
            logger.info(f"Loading {model_name}", status="Success")  # logger.init_ok
            toc = time.time()
            logger.info(
                f"Loading {model_name}: Took {toc-tic} seconds", status="Success"
            )  # logger.init_ok
            return True

    def load_esrgan(
        self,
        model_name,
    ):
        model_path = self.get_model_files(model_name)[0]["path"]
        sd = comfy.utils.load_torch_file(model_path)
        out = comfy_extras.chainner_models.model_loading.load_state_dict(sd).eval()
        return (out, )
