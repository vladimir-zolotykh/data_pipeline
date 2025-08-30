#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> list(yield_lognames("access-log-0108.*", "www"))
['access-log-0108.bz2', 'access-log-0108.gz']
>>>
"""
import io
import os
import re
import fnmatch
from typing import Generator
import gzip
import bz2

# import doctest


def yield_lognames(pattern: str, top: str) -> Generator[str, None, None]:
    """Log file filenames"""

    for dirpath, dirnames, filenames in os.walk(top):
        for fn in fnmatch.filter(filenames, pattern):
            yield os.path.join(dirpath, fn)


def yield_logopen(
    lognames: Generator[str, None, None],
) -> Generator[io.BufferedIOBase, None, None]:
    """Open log files"""

    fo: gzip.GzipFile | bz2.BZ2File
    for log in lognames:
        if log.endswith(".gz"):
            fo = gzip.open(log)
        elif log.endswith(".bz2"):
            fo = bz2.open(log)
        else:
            open(log)  # io.BufferedIOBase
        yield fo
        fo.close()


def yield_lines(
    logopens: Generator[io.BufferedIOBase, None, None],
) -> Generator[str, None, None]:
    """Lines from all chained log files"""

    for gen in logopens:
        # yield from gen
        for line in gen:
            yield line.decode("utf-8")


def filter_lines(
    pattern: str, lines: Generator[str, None, None]
) -> Generator[str, None, None]:
    for line in lines:
        if re.search(pattern, line):
            yield line


if __name__ == "__main__":
    # doctest.testmod()
    lognames = yield_lognames("access-log*.*", "www")
    openfiles = yield_logopen(lognames)
    lines = yield_lines(openfiles)
    for line in filter_lines("(?i)python", lines):
        print(line)
