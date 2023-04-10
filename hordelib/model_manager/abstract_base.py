from abc import ABC, abstractmethod, abstractproperty
from pathlib import Path
from typing import Any


class AbstractBaseModelManager(ABC):  # XXX
    path: str
    models: dict
    available_models: list
    loaded_models: dict
    tainted_models: list
    pkg: Any  # XXX Deprecated
    models_db_name: str
    models_path: Path
    cuda_available: bool
    cuda_devices: list
    recommended_gpu: list
    download_reference: bool
    remote_db: str

    @abstractmethod
    def init(self):  # XXX
        """"""

    # @abstractmethod
    # def load(self):  # XXX
    #     """"""
