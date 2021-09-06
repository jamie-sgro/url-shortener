from typing import Any, Union
from dataclasses import dataclass
from abc import ABC, abstractclassmethod


@dataclass
class DbAccessorResult:
    status: bool
    description: str
    value: Union[str, int, None] = None


class IDbAccessor(ABC):
    @abstractclassmethod
    def add(cls, name: str, key: str, value: Any) -> DbAccessorResult:
        ...

    @classmethod
    def add_overwrite(cls, name: str, key: str, value: Any) -> DbAccessorResult:
        ...

    @classmethod
    def increment(cls, name: str, key: str, value: int) -> DbAccessorResult:
        ...

    @abstractclassmethod
    def query(cls, name: str, key: str) -> DbAccessorResult:
        ...
