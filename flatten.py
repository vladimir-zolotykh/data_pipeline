#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK

nested_list = [
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


def flatten(items):
    return items


if __name__ == "__main__":
    flat_list = flatten(nested_list)
    print(flat_list)
