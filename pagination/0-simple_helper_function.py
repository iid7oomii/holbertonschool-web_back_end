#!/usr/bin/env python3
"""Pagination helper"""


def index_range(page: int, page_size: int) -> tuple:
    """Return start and end indexes for pagination"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
