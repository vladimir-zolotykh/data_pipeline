#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> list(yield_lognames("access-log-0108.*", "www"))
['access-log-0108.bz2', 'access-log-0108.gz']
>>>
"""
from typing import TextIO, cast
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
) -> Generator[TextIO, None, None]:
    """Open log files"""

    fo: TextIO
    for log in lognames:
        if log.endswith(".gz"):
            fo = cast(TextIO, gzip.open(log, "rt"))
        elif log.endswith(".bz2"):
            fo = cast(TextIO, bz2.open(log, "rt"))
        else:
            fo = open(log, "rt")
        yield fo
        fo.close()


def yield_lines(
    logopens: Generator[TextIO, None, None],
) -> Generator[str, None, None]:
    """Lines from all chained log files"""

    for gen in logopens:
        # yield from gen
        for line in gen:
            if isinstance(line, str):
                yield line
            else:
                yield line.decode("utf-8")


def filter_lines(
    pattern: str, lines: Generator[str, None, None]
) -> Generator[str, None, None]:
    for line in lines:
        if re.search(pattern, line):
            yield line


def filter_bytes_transfered(
    lines: Generator[str, None, None],
) -> Generator[str, None, None]:
    for line in lines:
        yield line.rsplit(None, 1)[1]


if __name__ == "__main__":
    # doctest.testmod()
    lognames = yield_lognames("access-log", "www")
    openfiles = yield_logopen(lognames)
    lines = yield_lines(openfiles)
    for line in filter_lines("UninstantiatedTemplates", lines):
        print(line, end="")
    # for line in filter_lines("(?i)python", lines):
    #     print(line)
    exit(0)
    total: int = 0
    for line in filter_bytes_transfered(lines):
        try:
            total += int(line)
        except ValueError:
            pass
    print(f"{total = }")
