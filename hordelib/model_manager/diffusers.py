import time

from loguru import logger

from hordelib.cache import get_cache_directory
from hordelib.comfy_horde import horde_load_checkpoint
from hordelib.config_path import get_hordelib_path
from hordelib.consts import MODEL_DB_NAMES, REMOTE_MODEL_DB, ModelCategoryNames
from hordelib.model_manager.base import BaseModelManager

# from nataili.util.voodoo import push_diffusers_pipeline_to_plasma


class DiffusersModelManager(BaseModelManager):
    def __init__(self, download_reference=False):  # XXX # Hack (download_reference)
        super().__init__(
            models_db_name=MODEL_DB_NAMES[ModelCategoryNames.diffusers],
            download_reference=download_reference,
        )

    def load(
        self,
        model_name,
        half_precision=True,  # XXX TODO
        gpu_id=0,  # XXX TODO
        cpu_only=False,  # XXX TODO
        voodoo=False,  # XXX TODO
    ):
        """
        model_name: str. Name of the model to load. See available_models for a list of available models.
        half_precision: bool. If True, the model will be loaded in half precision.
        gpu_id: int. The id of the gpu to use. If the gpu is not available, the model will be loaded on the cpu.
        cpu_only: bool. If True, the model will be loaded on the cpu. If True, half_precision will be set to False.
        voodoo: bool. Voodoo (Ray)
        """
        if model_name not in self.models:
            logger.error(f"{model_name} not found")
            return False
        if model_name not in self.available_models:
            logger.error(f"{model_name} not available")
            logger.info(
                f"Downloading {model_name}",
                status="Downloading",
            )  # logger.init_ok
            self.download_model(model_name)
            logger.info(
                f"{model_name} downloaded",
                status="Downloading",
            )  # logger.init_ok
        if model_name not in self.loaded_models:
            tic = time.time()
            logger.info(f"{model_name}", status="Loading")  # logger.init
            ckpt_path = self.get_model_files(model_name)[0]["path"]
            ckpt_path = f"{self.path}/{ckpt_path}"
            self.loaded_models[model_name] = horde_load_checkpoint(ckpt_path=ckpt_path)
            logger.info(f"Loading {model_name}", status="Success")  # logger.init_ok
            toc = time.time()
            logger.info(
                f"Loading {model_name}: Took {toc-tic} seconds",
                status="Success",
            )  # logger.init_ok
            return True
        return None
