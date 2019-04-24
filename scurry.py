# -*- coding: utf-8 -*-
"""A FizzBuzz configuration."""
from functools import partial

from fizzbuzz import byn, FizzBuzz

actions = (
    partial(byn, div=3, out='Three'),
    partial(byn, div=5, out='Five'),
)


def main():
    fb = FizzBuzz(actions)
    for i in range(1, 101):
        print(fb.response(i))

if __name__ == "__main__":
   main()
