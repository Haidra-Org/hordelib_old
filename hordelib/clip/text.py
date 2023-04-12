import hashlib
from concurrent.futures import ThreadPoolExecutor

import clip
import numpy as np
import torch
from loguru import logger

from hordelib.cache import Cache
from hordelib.utils.cast import autocast_cuda


class TextEmbed:
    def __init__(self, model_info, cache: Cache):
        """
        :param model: Loaded model from ModelManager
        :param cache: Cache object
        """
        self.model_info = model_info
        self.cache = cache
        self.executor = ThreadPoolExecutor(
            max_workers=1024,
            thread_name_prefix="SaveThread",
        )

    @autocast_cuda
    def _batch(self, text_list: list):
        for text in text_list:
            if isinstance(text["prompt"], bytes):
                text["prompt"] = text["prompt"].decode("utf-8")
            text["hash"] = hashlib.sha256(text["prompt"]).hexdigest()
        text_tokens = [
            clip.tokenize(text["prompt"], truncate=True).to(self.model_info["device"]) for text in text_list
        ]
        text_tokens = torch.cat(text_tokens, dim=0)
        with torch.no_grad():
            text_features = self.model_info["model"].encode_text(text_tokens).float()
        for text_embed_array, text in zip(text_features, text_list):
            self.executor.submit(self._save, text_embed_array, text["hash"])
            self.cache.add_sqlite_row(text["filename"], text["hash"], text["hash"])

    def _save(self, text_embed_array, text_hash):
        text_embed_array /= text_embed_array.norm(dim=-1, keepdim=True)
        np.save(
            f"{self.cache.cache_dir}/{text_hash}",
            text_embed_array.float().cpu().detach().numpy(),
        )

    @autocast_cuda
    def __call__(self, text: str, check_cache: bool = False, filename: str = None):
        """
        :param text: Text to embed
        :param check_cache: Check cache for text
        :param filename: Filename to save to cache
        If text is not in cache, embed it and save it to cache
        """
        if isinstance(text, bytes):
            text = text.decode("utf-8")
        text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        if check_cache:
            cached = self.cache.get(file_hash=text_hash)
            if cached:
                return cached
        text_tokens = clip.tokenize([text], truncate=True).to(self.model_info["device"])
        with torch.no_grad():
            text_features = self.model_info["model"].encode_text(text_tokens).float()
        text_features /= text_features.norm(dim=-1, keepdim=True)
        text_embed_array = text_features.cpu().detach().numpy()
        if filename:
            np.save(f"{self.cache.cache_dir}/{text_hash}", text_embed_array)
            self.cache.add_sqlite_row(filename, text_hash, text_hash)
            return None

        np.save(f"{self.cache.cache_dir}/{text_hash}", text_embed_array)
        self.cache.add_sqlite_row(text, text_hash, text_hash)
        return None
