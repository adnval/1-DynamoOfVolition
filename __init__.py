import inspect
from collections import abc
from types import FunctionType
from typing import Any, Dict, Iterator, Optional


class DynamicScope(abc.Mapping):
    def __init__(self):
        self.env: Dict[str, Optional[Any]] = {}


def get_dynamic_re() -> DynamicScope:
    return None
