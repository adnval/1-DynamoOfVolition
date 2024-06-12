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
    refEnvironment = DynamicScope()
    for statement in inspect.stack():
        # Gets the dictionary of variables for the function
        frameVars = statement[0].f_locals
        for var in frameVars:
            # Checks to omit the variable if it is of NoneType
            if frameVars[var] is None or var in refEnvironment.env:
                continue
            refEnvironment[var] = frameVars[var]
    return refEnvironment
