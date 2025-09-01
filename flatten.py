#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from collections.abc import Iterable


nested_list_gemini = [
    [
        "first_level_string",
        "another_string",
        ["one", 2, "three", 4],
    ],
    [
        10,
        20,
        ["apple", 50, "banana", 60],
    ],
    [["a", "b", "c", "d"]],
]
nested_list_gpt = [
    [["apple", "banana", 1, 2], ["cherry", 3, 4, "date"]],
    [["eggplant", 5, "fig"], ["grape", ["honeydew", 6, 7]]],
]


def flatten(items):
    """
    >>> list(flatten(nested_list_gpt))
    ['apple', 'banana', 1, 2, 'cherry', 3, 4, 'date', 'eggplant', 5, 'fig', 'grape', 'honeydew', 6, 7]
    >>> list(flatten(nested_list_gemini))
    ['first_level_string', 'another_string', 'one', 2, 'three', 4, 10, 20, 'apple', 50, 'banana', 60, 'a', 'b', 'c', 'd']
    """

    for item in items:
        if isinstance(item, Iterable) and not type(item) in (str, bytes):
            yield from flatten(item)
        else:
            yield item


if __name__ == "__main__":
    import doctest

    doctest.testmod()
