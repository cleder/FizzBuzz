# -*- coding: utf-8 -*-
"""A generic configurable FizzBuzz."""

from functools import partial
from typing import Callable, List, Optional, Tuple, cast


def byn(number: int, div: int, out: str) -> str:
    assert isinstance(number, int)
    assert isinstance(div, int)
    if number % div == 0:
        return out
    return ""


callback = Callable[[int], str]


class FizzBuzz(object):

    _actions: Tuple[callback, ...] = (
        cast(callback, partial(byn, div=3, out="fizz")),
        cast(callback, partial(byn, div=5, out="buzz")),
    )

    def __init__(
        self,
        actions: Optional[Tuple[callback, ...]] = None,
        default_action: Optional[callback] = None,
    ) -> None:
        if actions:
            self._actions = actions
        if default_action:
            self._default_action = default_action
        else:
            self._default_action = cast(callback, str)

    def response(self, number: int) -> List[str]:
        rlist = [result for action in self._actions if (result := action(number))]
        if not rlist:
            return [self._default_action(number)]
        return rlist
