from abc import ABC, abstractclassmethod

class IDbAccessor(ABC):
    @abstractclassmethod
    def add(cls): ...

    @abstractclassmethod
    def query(cls): ...