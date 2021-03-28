# -*- coding: utf-8 -*-
"""A generic configurable FizzBuzz."""

from functools import partial
from typing import Callable, Optional, Tuple, cast


def byn(number: int, div: int, out: str) -> Tuple[str, bool]:
    assert isinstance(number, int)
    assert isinstance(div, int)
    if number % div == 0:
        return out, False
    return "", False


callback = Callable[[int], Tuple[str, bool]]


class FizzBuzz(object):

    _actions: Tuple[callback, ...] = (
        cast(callback, partial(byn, div=3, out="fizz")),
        cast(callback, partial(byn, div=5, out="buzz")),
    )

    def __init__(
        self,
        actions: Optional[Tuple[callback, ...]] = None,
        default_action: Optional[Callable[[int], str]] = None,
    ) -> None:
        if actions:
            self._actions = actions
        if default_action:
            self._default_action = default_action
        else:
            self._default_action = cast(Callable[[int], str], str)

    def response(self, number: int) -> str:
        rstr = ""
        for action in self._actions:
            astr, is_return = action(number)
            if is_return:
                return astr
            rstr += astr
        if not rstr:
            rstr = self._default_action(number)
        return rstr
