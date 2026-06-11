import functools
from typing import Any, Self

import setdoc

__all__ = [
    "classdecorator",
    "getdecorator",
    "getproperty",
]


def classdecorator(cls: Any, /, **kwargs: Any) -> Any:
    "This decorator adds keyaliases to cls and then returns cls."
    alias: str
    key: Any
    pro: property
    for alias, key in kwargs.items():
        pro = getproperty(key)
        setattr(cls, alias, pro)
    return cls


def getdecorator(**kwargs: Any) -> functools.partial:
    "This function returns a keyalias decorator for a class."
    return functools.partial(classdecorator, **kwargs)


def getproperty(key: Any) -> property:
    "This function returns a new keyalias property."

    @setdoc.basic
    def fget(
        self: Self, # type: ignore[misc]
        /,
    ) -> Any:
        return self[key]

    @setdoc.basic
    def fset(
        self: Self, # type: ignore[misc]
        value: Any, 
        /,
    ) -> None:
        self[key] = value

    @setdoc.basic
    def fdel(
        self: Self, # type: ignore[misc]
        /,
    ) -> None:
        del self[key]

    return property(fget, fset, fdel, "self[%r]" % key)
