from abc import ABC, abstractclassmethod


class IDbAccessor(ABC):
    @abstractclassmethod
    def add(cls, name: str, key: str):
        ...

    @abstractclassmethod
    def query(cls, name: str, key: str):
        ...
