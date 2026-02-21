#!/usr/bin/env python3
"""
Module that defines an asynchronous coroutine async_comprehension.
"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension
    over async_generator and returns them.
    """
    return [i async for i in async_generator()]
