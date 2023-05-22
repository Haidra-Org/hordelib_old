import hashlib
import json
import os
import re
import threading
import time
import typing
from collections import deque
from datetime import datetime
from enum import Enum

import requests
from fuzzywuzzy import fuzz
from loguru import logger
from typing_extensions import override

from hordelib.consts import MODEL_CATEGORY_NAMES, MODEL_DB_NAMES, MODEL_FOLDER_NAMES
from hordelib.model_manager.base import BaseModelManager
from hordelib.utils.sanitizer import Sanitizer


class DOWNLOAD_SIZE_CHECK(str, Enum):
    everything = "everything"
    top = "top"
    adhoc = "adhoc"


class LoraModelManager(BaseModelManager):

    LORA_API = "https://civitai.com/api/v1/models?types=LORA&sort=Highest%20Rated"
    MAX_RETRIES = 10
    MAX_DOWNLOAD_THREADS = 3  # max concurrent downloads
    RETRY_DELAY = 5  # seconds
    REQUEST_METADATA_TIMEOUT = 30  # seconds
    REQUEST_DOWNLOAD_TIMEOUT = 300  # seconds

    def __init__(
        self,
        download_reference=True,
        allowed_top_lora_storage=5120,
        allowed_adhoc_lora_storage=1024,
        download_wait=True,
    ):

        self._max_top_disk = allowed_top_lora_storage
        self._max_adhoc_disk = allowed_adhoc_lora_storage
        self._data = None
        self._next_page_url = None
        self._mutex = threading.Lock()
        self._file_count = 0
        self._download_threads = []
        self._download_queue = deque()
        self._thread = None
        self.done = False
        self.model_data = []
        # Not yet handled, as we need a global reference to search through.
        self._adhoc_loras = set()
        self._adhoc_mutex = {}
        self._download_wait = download_wait

        super().__init__(
            modelFolder=MODEL_FOLDER_NAMES[MODEL_CATEGORY_NAMES.lora],
            models_db_name=MODEL_DB_NAMES[MODEL_CATEGORY_NAMES.lora],
            download_reference=download_reference,
        )

    def loadModelDatabase(self, list_models=False):
        if self.model_reference:
            logger.info(
                (
                    "Model reference was already loaded."
                    f" Got {len(self.model_reference)} models for {self.models_db_name}."
                ),
            )
            logger.info("Reloading model reference...")

        if self.download_reference:
            self.download_model_reference()
            logger.info("Lora reference download begun asynchronously.")
        else:
            self.model_reference = json.loads((self.models_db_path).read_text())
            logger.info(
                " ".join(
                    [
                        "Loaded model reference from disk.",
                        f"Got {len(self.model_reference)} models for {self.models_db_name}.",
                    ],
                ),
            )

    def download_model_reference(self):
        # We have to wipe it, as we are going to be adding it it instead of replacing it
        self.model_reference = {}
        self.download()

    def _get_json(self, url):
        retries = 0
        while retries <= self.MAX_RETRIES:
            try:
                response = requests.get(url, timeout=self.REQUEST_METADATA_TIMEOUT)
                response.raise_for_status()
                # Attempt to decode the response to JSON
                return response.json()

            except (requests.HTTPError, requests.ConnectionError, requests.Timeout, json.JSONDecodeError):
                retries += 1
                if retries <= self.MAX_RETRIES:
                    time.sleep(self.RETRY_DELAY)
                else:
                    # Max retries exceeded, give up
                    return None

            except Exception as e:
                # Failed badly
                logger.error(f"LORA download failed {e}")
                return None

    def _get_more_items(self):
        if not self._data:
            url = self.LORA_API
        else:
            url = self._next_page_url

        # This may be the end of the road, unlikely but...
        if not url:
            logger.warning("End of LORA data reached")
            self.done = True
        else:
            # Get the actual item data
            items = self._get_json(url)
            if items:
                self._data = items
                self._next_page_url = self._data.get("metadata", {}).get("nextPage", "")
            else:
                # We failed to get more items
                logger.error("Failed to download all LORA data even after retries.")
                self._data = None
                self._next_page_url = None  # give up

    def _parse_civitai_lora_data(self, item):
        """Return a simplified dictionary with the information we actually need about a lora"""
        lora = {
            "name": "",
            "sha256": "",
            "filename": "",
            "id": "",
            "url": "",
            "triggers": [],
            "size_mb": 0,
        }
        # get top version
        try:
            version = item.get("modelVersions", {})[0]
        except IndexError:
            version = {}
        # Get model triggers
        triggers = version.get("trainedWords", [])
        # get first file that is a primary file and a safetensor
        for file in version.get("files", {}):
            if file.get("primary", False) and file.get("name", "").endswith(".safetensors"):
                lora["name"] = Sanitizer.sanitise_model_name(item.get("name", ""))
                lora["filename"] = f'{Sanitizer.sanitise_filename(lora["name"])}.safetensors'
                lora["sha256"] = file.get("hashes", {}).get("SHA256")
                try:
                    lora["size_mb"] = round(file.get("sizeKB", 0) / 1024)
                except TypeError:
                    lora["size_mb"] = 144  # guess common case of 144MB, it's not critical here
                lora["url"] = file.get("downloadUrl", "")
                lora["triggers"] = triggers
                break
        # If we don't have everything required, fail
        if not lora.get("sha256") or not lora.get("filename") or not lora.get("url") or not lora.get("triggers"):
            return
        # Fixup A1111 centric triggers
        for i, trigger in enumerate(lora["triggers"]):
            if re.match("<lora:(.*):.*>", trigger):
                lora["triggers"][i] = re.sub("<lora:(.*):.*>", "\\1", trigger)
        return lora

    def _download_thread(self):
        # We try to download the LORA. There are tens of thousands of these things, we aren't
        # picky if downloads fail, as they often will if civitai is the host, we just move on to
        # the next one
        while True:
            # Endlessly look for files to download and download them
            try:
                lora = self._download_queue.popleft()
            except IndexError:
                # Nothing in the queue
                time.sleep(2)
                continue

            # Download the lora
            os.makedirs(self.modelFolderPath, exist_ok=True)
            retries = 0
            while retries <= self.MAX_RETRIES:
                try:
                    # Just before we download this file, check if we already have it
                    filename = os.path.join(self.modelFolderPath, lora["filename"])
                    hashfile = f"{os.path.splitext(filename)[0]}.sha256"
                    if os.path.exists(filename) and os.path.exists(hashfile):
                        # Check the hash
                        with open(hashfile) as infile:
                            try:
                                hashdata = infile.read().split()[0]
                            except (IndexError, OSError, IOError, PermissionError):
                                hashdata = ""
                        if hashdata.lower() == lora["sha256"].lower():
                            # we already have this lora, consider it downloaded
                            logger.debug(f"Already have LORA {lora['filename']}")
                            with self._mutex:
                                self.model_data.append(lora)
                                # We store as lower to allow case-insensitive search
                                self.model_reference[lora["name"].lower()] = lora
                                if len(self._adhoc_mutex) == 0:
                                    if self.calculate_downloaded_loras(DOWNLOAD_SIZE_CHECK.top) > self._max_top_disk:
                                        self.done = True
                                else:
                                    # Normally this should never happen unless the user manually
                                    # reduced their max size in the meantime
                                    if (
                                        self.calculate_downloaded_loras(DOWNLOAD_SIZE_CHECK.adhoc)
                                        > self._max_adhoc_disk
                                    ):
                                        self.delete_oldest_lora()
                                self.save_cached_reference_to_disk()
                            break

                    logger.info(f"Starting download of LORA {lora['filename']}")
                    response = requests.get(lora["url"], timeout=self.REQUEST_DOWNLOAD_TIMEOUT)
                    response.raise_for_status()
                    # Check the data hash
                    hash_object = hashlib.sha256()
                    hash_object.update(response.content)
                    sha256 = hash_object.hexdigest()
                    if sha256.lower() == lora["sha256"].lower():
                        # wow, we actually got a valid file, save it
                        with open(filename, "wb") as outfile:
                            outfile.write(response.content)
                        # Save the hash file
                        with open(hashfile, "wt") as outfile:
                            outfile.write(f"{sha256} *{lora['filename']}")

                        # Shout about it
                        logger.info(f"Downloaded LORA {lora['filename']} ({lora['size_mb']} MB)")
                        # Maybe we're done
                        with self._mutex:
                            self.model_data.append(lora)
                            # We store as lower to allow case-insensitive search
                            self.model_reference[lora["name"].lower()] = lora
                            lora["last_used"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
                            if len(self._adhoc_mutex) == 0:
                                if self.calculate_downloaded_loras(DOWNLOAD_SIZE_CHECK.top) > self._max_top_disk:
                                    self.done = True
                            else:
                                if self.calculate_downloaded_loras(DOWNLOAD_SIZE_CHECK.adhoc) > self._max_adhoc_disk:
                                    self.delete_oldest_lora()
                            self.save_cached_reference_to_disk()
                        break
                    else:
                        # We will retry
                        logger.debug(f"Downloaded LORA file for {lora['filename']} didn't match hash")

                except (requests.HTTPError, requests.ConnectionError, requests.Timeout, json.JSONDecodeError) as e:
                    # We will retry
                    logger.debug(f"Error downloading {lora['filename']} {e}")

                except Exception as e:
                    # Failed badly, ignore and retry
                    logger.debug(f"Fatal error downloading {lora['filename']} {e}")

                retries += 1
                logger.debug(f"Retry of LORA file download for {lora['filename']}")
                if retries > self.MAX_RETRIES:
                    break  # fail

                time.sleep(self.RETRY_DELAY)

    def _download_lora(self, lora):
        with self._mutex:
            # Start download threads if they aren't already started
            while len(self._download_threads) < self.MAX_DOWNLOAD_THREADS:
                thread = threading.Thread(target=self._download_thread, daemon=True)
                thread.start()
                self._download_threads.append(thread)

            # Add this lora to the download queue
            self._download_queue.append(lora)

    def _process_items(self):
        # i.e. given a bunch of LORA item metadata, download them
        for item in self._data.get("items", []):
            lora = self._parse_civitai_lora_data(item)
            if lora:
                self._file_count += 1
                # Allow a queue of 20% larger than the max disk space as we'll lose some
                if self.calculate_download_queue() + self.calculate_downloaded_loras() > self._max_top_disk:
                    return
                # We have valid lora data, download it
                self._download_lora(lora)

    def _start_processing(self):

        self.done = False

        while not self.done:

            # Get some items to download
            self._get_more_items()

            # If we have some items to process, process them
            if self._data:
                self._process_items()

    def download(self):
        """Start up a background thread downloading and return immediately"""

        # Don't start if we're already busy doing something
        if self._thread:
            return

        # Start processing in a background thread
        self._thread = threading.Thread(target=self._start_processing, daemon=True)
        self._thread.start()
        # Wait for completion of our threads if requested
        # rtr = 0
        if self._download_wait:
            while self._thread.is_alive():
                time.sleep(0.5)
                # rtr += 1
                # if rtr > 15:
                #     raise Exception

    def get_lora_filename(self, model_name: str):
        lora_name = self.fuzzy_find_lora(model_name)
        if not lora_name:
            return None
        return self.model_reference[lora_name]["filename"]

    def get_model(self, model_name: str):
        lora_name = self.fuzzy_find_lora(model_name)
        if not lora_name:
            return None
        return self.model_reference[lora_name]

    def save_cached_reference_to_disk(self):
        with open(self.models_db_path, "wt", encoding="utf-8", errors="ignore") as outfile:
            outfile.write(json.dumps(self.model_reference, indent=4))

    def calculate_downloaded_loras(self, mode=DOWNLOAD_SIZE_CHECK.everything):
        total_size = 0
        for lora in self.model_reference.values():
            if mode == DOWNLOAD_SIZE_CHECK.top and lora["name"] in self._adhoc_loras:
                continue
            if mode == DOWNLOAD_SIZE_CHECK.adhoc and lora["name"] not in self._adhoc_loras:
                continue
            total_size += lora["size_mb"]
        return total_size

    def calculate_download_queue(self):
        total_queue = 0
        for lora in self._download_queue:
            total_queue += lora["size_mb"]
        return total_queue

    def find_oldest_adhoc_lora(self):
        oldest_lora: str = None
        oldest_datetime: datetime = None
        for lora in self._adhoc_loras:
            lora_datetime = datetime.strptime(self.model_reference[lora]["last_used"], "%Y-%m-%d %H:%M:%S")
            if not oldest_lora:
                oldest_lora = lora
                oldest_datetime = lora_datetime
                continue
            if oldest_datetime > lora_datetime:
                oldest_lora = lora
                oldest_datetime = lora_datetime
        return oldest_lora

    def delete_oldest_lora(self):
        oldest_lora = self.find_oldest_adhoc_lora()
        if not oldest_lora:
            return
        filename = os.path.join(self.modelFolderPath, self.model_reference[oldest_lora]["filename"])
        os.remove(filename)
        del self.model_reference[oldest_lora]
        del self._adhoc_loras[oldest_lora]

    def fuzzy_find_lora(self, lora_name):
        sname = Sanitizer.remove_version(lora_name).lower()
        if sname in self.model_reference:
            return sname
        for lora in self.model_reference:
            if sname in lora:
                return sname
        for lora in self.model_reference:
            if fuzz.ratio(lora, self.model_reference) > 90:
                return sname
        return None

    @override
    def is_local_model(self, model_name):
        return self.fuzzy_find_lora(model_name) is not None

    @override
    def modelToRam(
        self,
        model_name: str,
        **kwargs,
    ) -> dict[str, typing.Any]:
        pass
