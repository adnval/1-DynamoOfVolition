import inspect
from collections import abc
from types import FunctionType
from typing import Any, Dict, Iterator, Optional


class DynamicScope(abc.Mapping):
    def __init__(self):
        self.env: Dict[str, Optional[Any]] = {}

    # Method to access the value given a key
    def __getitem__(self, key: str) -> Optional[Any]:
        if not key in self.env:
            raise NameError(f"Name '{key}' is not defined")
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
    refEnvironment = DynamicScope()
    for frameInfo in inspect.stack()[1:]:
        frameObject = frameInfo[0]
        functionName = frameObject.f_code.co_name
        vars = frameObject.f_locals
        freeVars = frameObject.f_code.co_freevars
        for var in vars:
            if var in refEnvironment.env or vars[var] is None or var in freeVars:
                continue
            refEnvironment[var] = vars[var]
    return refEnvironment
