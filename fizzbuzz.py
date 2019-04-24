# -*- coding: utf-8 -*-
"""A generic configurable FizzBuzz."""

from functools import partial


def byn(number, div, out):
    assert isinstance(number, int)
    assert isinstance(div, int)
    if number % div == 0:
        return out
    return ''


def to_str(number):
    return str(number)


class FizzBuzz(object):

    _actions = (
        partial(byn, div=3, out='fizz'),
        partial(byn, div=5, out='buzz'),
    )

    _default_action = partial(to_str)

    def __init__(self, actions=None, default_action=None):
        if actions:
            self._actions = actions
        if default_action:
            self._default_action = default_action

    def response(self, number):
        rstr = ''
        for action in self._actions:
            rstr += action(number)
        if not rstr:
            rstr = self._default_action(number)
        return rstr
