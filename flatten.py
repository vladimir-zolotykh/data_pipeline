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
nested_list_deepseek = [
    "Level 1 - String",
    100,
    [
        "Level 2 - String",
        200,
        ["Level 3 - String", 300, "Another level 3 string", 3.14],
        2.5,
    ],
    400,
    ["Second level 2 branch", ["Deep string", 999, ["Level 4 (bonus!)", 42]]],
]


def flatten(items, ignore_types=(str, bytes)):
    """
    >>> list(flatten(nested_list_gpt))
    ['apple', 'banana', 1, 2, 'cherry', 3, 4, 'date', 'eggplant', 5, 'fig', 'grape', 'honeydew', 6, 7]
    >>> list(flatten(nested_list_gemini))
    ['first_level_string', 'another_string', 'one', 2, 'three', 4, 10, 20, 'apple', 50, 'banana', 60, 'a', 'b', 'c', 'd']
    >>> list(flatten(nested_list_deepseek))
    ['Level 1 - String', 100, 'Level 2 - String', 200, 'Level 3 - String', 300, 'Another level 3 string', 3.14, 2.5, 400, 'Second level 2 branch', 'Deep string', 999, 'Level 4 (bonus!)', 42]
    """

    for item in items:
        if isinstance(item, Iterable) and not isinstance(item, ignore_types):
            yield from flatten(item)
        else:
            yield item


if __name__ == "__main__":
    import doctest

    doctest.testmod()
