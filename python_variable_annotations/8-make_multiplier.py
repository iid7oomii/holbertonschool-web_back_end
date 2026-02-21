#!/usr/bin/env python3
"""
Module that defines a type-annotated function make_multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier.
    """
    def multiplier_function(n: float) -> float:
        """
        Multiplies a float by the multiplier.
        """
        return n * multiplier

    return multiplier_function
