from typing import Any, Final

from keyalias.core import classdecorator, getdecorator, getproperty

__all__ = [
    "classdecorator",
    "getdecorator",
    "getproperty",
    "keyalias",
]
keyalias: Final[Any] = getdecorator  # legacy
