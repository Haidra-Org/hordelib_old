import copy
import os
import pickle
import typing

from typing_extensions import override

from hordelib.comfy_horde import horde_load_checkpoint
from hordelib.consts import MODEL_CATEGORY_NAMES, MODEL_DB_NAMES, MODEL_FOLDER_NAMES
from hordelib.model_manager.base import BaseModelManager


class CompVisModelManager(BaseModelManager):
    def __init__(
        self,
        download_reference=False,
        # custom_path="models/custom",  # XXX Remove this and any others like it?
    ):
        super().__init__(
            modelFolder=MODEL_FOLDER_NAMES[MODEL_CATEGORY_NAMES.compvis],
            models_db_name=MODEL_DB_NAMES[MODEL_CATEGORY_NAMES.compvis],
            download_reference=download_reference,
        )

    @override
    def modelToRam(
        self,
        model_name: str,
        **kwargs,
    ) -> dict[str, typing.Any]:

        embeddings_path = os.getenv("HORDE_MODEL_DIR_EMBEDDINGS", "./")

        return horde_load_checkpoint(
            ckpt_path=self.getFullModelPath(model_name),
            embeddings_path=embeddings_path,
        )

    def can_cache_on_disk(self):
        """Can this of type model be cached on disk?"""
        return True

    def move_to_disk_cache(self, model_name):
        # FIXME this is a nonsense location, just testing
        cachedir = os.getenv("RAY_TEMP_DIR", "./ray")

        cachefile = os.path.join(cachedir, model_name)
        # Create cache directory if it doesn't already exist
        if not os.path.isdir(cachedir):
            os.makedirs(cachedir, exist_ok=True)
        # Serialise our objects
        if not os.path.exists(cachefile + ".model"):
            with open(cachefile + ".model", "wb") as cache:
                pickle.dump(self.loaded_models[model_name]["model"], cache, protocol=pickle.HIGHEST_PROTOCOL)
        if not os.path.exists(cachefile + ".vae"):
            with open(cachefile + ".vae", "wb") as cache:
                pickle.dump(self.loaded_models[model_name]["vae"], cache, protocol=pickle.HIGHEST_PROTOCOL)
        if not os.path.exists(cachefile + ".clip"):
            with open(cachefile + ".clip", "wb") as cache:
                pickle.dump(self.loaded_models[model_name]["clip"], cache, protocol=pickle.HIGHEST_PROTOCOL)
        # Remember the cache locations
        modeldata = copy.copy(self.loaded_models[model_name])
        modeldata["model"] = cachefile + ".model"
        modeldata["vae"] = cachefile + ".vae"
        modeldata["clip"] = cachefile + ".clip"
        # Remove from ram
        self.remove_model_from_ram(model_name)
        # Point the model to the cache
        self.loaded_models[model_name] = modeldata
