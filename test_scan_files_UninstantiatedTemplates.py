#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import subprocess
import textwrap


def test_scan_files_output():
    result = subprocess.run(
        ["python", "scan_files.py"],
        capture_output=True,
        text=True,
        check=True,
    )
    expected = textwrap.dedent(
        """\
        75.165.49.150 - - [24/Feb/2008:02:30:06 -0600] "GET /cgi-bin/wiki.pl?UninstantiatedTemplates HTTP/1.1" 200 2091
        130.79.100.39 - - [25/Feb/2008:02:41:24 -0600] "GET /cgi-bin/wiki.pl?UninstantiatedTemplates HTTP/1.1" 200 2091
        75.165.49.150 - - [24/Feb/2008:02:30:06 -0600] "GET /cgi-bin/wiki.pl?UninstantiatedTemplates HTTP/1.1" 200 2091
        130.79.100.39 - - [25/Feb/2008:02:41:24 -0600] "GET /cgi-bin/wiki.pl?UninstantiatedTemplates HTTP/1.1" 200 2091
    """
    )
    assert result.stdout == expected
