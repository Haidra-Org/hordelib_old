import os
import time

from loguru import logger

from hordelib.comfy_horde import horde_load_checkpoint
from hordelib.consts import (
    MODEL_DB_NAMES,
    MODEL_FOLDER_NAMES,
    ModelCategoryNames,
)
from hordelib.model_manager.base import BaseModelManager


class CompVisModelManager(BaseModelManager):
    def __init__(
        self,
        download_reference=True,
        # custom_path="models/custom",  # XXX Remove this and any others like it?
    ):
        super().__init__(
            modelFolder=MODEL_FOLDER_NAMES[ModelCategoryNames.compvis],
            models_db_name=MODEL_DB_NAMES[ModelCategoryNames.compvis],
            download_reference=download_reference,
        )

    def load(
        self,
        model_name: str,
        output_vae=True,
        output_clip=True,
    ):
        """
        model_name: str. Name of the model to load. See available_models for a list of available models.
        """
        if model_name not in self.models:
            logger.error(f"{model_name} not found")
            return False
        if model_name not in self.available_models:
            logger.error(f"{model_name} not available")
            self.download_model(model_name)
            logger.info(f"{model_name}", status="Downloaded")  # logger.init_ok
        if model_name not in self.loaded_models:
            tic = time.time()
            logger.info(f"{model_name}", status="Loading")  # logger.init
            embeddings_path = os.getenv("HORDE_MODEL_DIR_EMBEDDINGS", "./")
            ckpt_path = self.get_model_files(model_name)[0]["path"]  # XXX Refactor
            ckpt_path = f"{self.path}/{ckpt_path}"
            self.loaded_models[model_name] = horde_load_checkpoint(
                ckpt_path=ckpt_path,
                embeddings_path=embeddings_path,
                output_vae=output_vae,
                output_clip=output_clip,
            )
            toc = time.time()
            logger.info(
                f"{model_name}: {round(toc-tic,2)} seconds",
                status="Loaded",
            )  # logger.init_ok
            return True
        return None
