#!/usr/bin/python3
"""read_file.py"""


def read_file(filename=""):

    with open(filename, "r", encoding='utf-8') as f:
        content = f.read()
        print(content)
        f.closed
