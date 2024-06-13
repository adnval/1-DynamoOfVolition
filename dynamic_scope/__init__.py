import inspect
from collections import abc
from types import FunctionType
from typing import Any, Dict, Iterator, Optional


class DynamicScope(abc.Mapping):
    """Encapsulates a dynamic reference environment.

    Defines a dictionary of variable names and values at a given statement.
    """

    def __init__(self):
        self.env: Dict[str, Optional[Any]] = {}

    """Returns the value of the key."""

    def __getitem__(self, key: str) -> Optional[Any]:
        # Handle nonexistent variables that are attempting to be accessed
        if not key in self.env:
            raise NameError(f"Name '{key}' is not defined")
        return self.env.__getitem__(key)

    """Adds a key-value pair to the reference environment."""

    def __setitem__(self, key: str, value: Optional[Any]):
        self.env.__setitem__(key, value)

    """Deletes a key-value pair from the reference environment."""

    def __delitem__(self, key: str):
        self.env.__delitem__(key)

    """Returns an iterator for the reference environment."""

    def __iter__(self) -> Iterator:
        return self.env.__iter__()

    """Returns the length of the reference environment."""

    def __len__(self) -> int:
        return self.env.__len__()


def get_dynamic_re() -> DynamicScope:
    refEnvironment = DynamicScope()
    # Starts iterating from index 1 for get_dynamic_re to skip itself
    for frameInfo in inspect.stack()[1:]:
        frameObject = frameInfo[0]
        vars = frameObject.f_locals
        freeVars = frameObject.f_code.co_freevars
        for var in vars:
            # Ignores existing, none-valued, and free variables respectively
            if var in refEnvironment.env or vars[var] is None or var in freeVars:
                continue
            refEnvironment[var] = vars[var]
    return refEnvironment
