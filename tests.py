# -*- coding: utf-8 -*-
"""Test FizzBuzz."""
from functools import partial
from unittest import TestCase

from fizzbuzz import byn, FizzBuzz
import pytest

class ByNTest(TestCase):

    def test_number_int(self):
        """Raise an assertion error when not an integer is passed."""
        with self.assertRaises(AssertionError):
            byn(0.1, 2, None)
        with self.assertRaises(AssertionError):
            byn(1, 0.2, None)

    def test_happy(self):
        """Test the happy path."""
        for i in range(3, 34, 3):
            assert byn(i, 3, 'xxx') == 'xxx'

    def test_happy_default(self):
        """Test the happy path."""
        for i in range(1, 99, 2):
            assert byn(i, 2, 'xxx') == ''


def xxx(*args, **kwargs):
    return 'xxx'

class FBTest(TestCase):

    def setUp(self):
        """Setup common stuff."""
        self.actions = (
            partial(byn, div=3, out='three'),
            partial(byn, div=5, out='five'),
            partial(byn, div=11, out='eleven'),
        )

    def test_classic(self):
        """Classic Fizzbuzz."""
        fb = FizzBuzz()
        assert fb.response(3) == 'fizz'
        assert fb.response(5) == 'buzz'
        assert fb.response(15) == 'fizzbuzz'
        assert fb.response(2) =='2'

    def test_custom(self):
        fb = FizzBuzz(self.actions)
        assert fb.response(3) == 'three'
        assert fb.response(5) == 'five'
        assert fb.response(11) == 'eleven'
        assert fb.response(15) == 'threefive'
        assert fb.response(2) == '2'
        assert fb.response(165) == 'threefiveeleven'

    def test_custom_default(self):
        fb = FizzBuzz(default_action=xxx)
        for i in range(0, 100):
            assert fb.response(i) in ['xxx', 'fizz', 'buzz', 'fizzbuzz']
