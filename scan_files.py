#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> list(yield_lognames("access-log-0108.*", "www"))
['access-log-0108.bz2', 'access-log-0108.gz']
>>>
"""
import os
import fnmatch
from typing import Generator
import doctest


def yield_lognames(pattern: str, top: str) -> Generator[str, None, None]:
    for dirpath, dirnames, filenames in os.walk(top):
        for fn in fnmatch.filter(filenames, pattern):
            yield fn


if __name__ == "__main__":
    doctest.testmod()
