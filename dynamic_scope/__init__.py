import inspect
from collections import abc
from types import FunctionType
from typing import Any, Dict, Iterator, Optional


class DynamicScope(abc.Mapping):
    def __init__(self):
        self.env: Dict[str, Optional[Any]] = {}

    # Method to access the value given a key
    def __getitem__(self, key: str) -> Optional[Any]:
        return self.env[key]

    # Method to return an interator object for the reference environment
    def __iter__(self) -> Any:
        return iter(self.env)

    # Method to return the amount of items for the reference environment
    def __len__(self) -> int:
        return len(self.env)


def get_dynamic_re() -> DynamicScope:
    referenceEnvironment = DynamicScope()
    return referenceEnvironment
