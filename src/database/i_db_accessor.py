from typing import Any
from abc import ABC, abstractclassmethod


class IDbAccessor(ABC):
    @abstractclassmethod
    def add(cls, name: str, key: str, value: Any):
        ...

    @abstractclassmethod
    def query(cls, name: str, key: str):
        ...
