import inspect
from collections import abc
from types import FunctionType
from typing import Any, Dict, Iterator, Optional


class DynamicScope(abc.Mapping):
    def __init__(self):
        self.env: Dict[str, Optional[Any]] = {}

    # Method to access the value given a key
    def __getitem__(self, key: str) -> Optional[Any]:
        return self.env.__getitem__(key)

    # Method to set a key-value pair in the reference environment
    def __setitem__(self, key: str, value: Optional[Any]):
        self.env.__setitem__(key, value)

    # Method to delete a key-value pair in the reference environment
    def __delitem__(self, key: str):
        self.env.__delitem__(key)

    # Method to return an interator object for the reference environment
    def __iter__(self) -> Iterator:
        return self.env.__iter__()

    # Method to return the amount of items for the reference environment
    def __len__(self) -> int:
        return self.env.__len__()


def get_dynamic_re() -> DynamicScope:
    referenceEnvironment = DynamicScope()
    return referenceEnvironment
