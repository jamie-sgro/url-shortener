from typing import Any, Union
from dataclasses import dataclass
from abc import ABC, abstractclassmethod


@dataclass
class DbAccessorResult:
    status: bool
    description: str
    value: Union[str, bytes, None] = None


class IDbAccessor(ABC):
    @abstractclassmethod
    def add(cls, name: str, key: str, value: Any) -> DbAccessorResult:
        ...

    @abstractclassmethod
    def query(cls, name: str, key: str) -> DbAccessorResult:
        ...
