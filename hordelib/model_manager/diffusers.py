from hordelib.comfy_horde import horde_load_checkpoint
from hordelib.consts import MODEL_CATEGORY_NAMES, MODEL_DB_NAMES
from hordelib.model_manager.base import BaseModelManager

# from nataili.util.voodoo import push_diffusers_pipeline_to_plasma


class DiffusersModelManager(BaseModelManager):
    def __init__(self, download_reference=False):
        super().__init__(
            models_db_name=MODEL_DB_NAMES[MODEL_CATEGORY_NAMES.diffusers],
            download_reference=download_reference,
        )

    def modelToRam(self, model_name: str, **kwargs):
        return horde_load_checkpoint(
            ckpt_path=self.getFullModelPath(model_name),
        )
