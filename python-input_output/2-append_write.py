#!/usr/bin/python3
'''apprend_write
'''


def append_write(filename="", text=""):
    """Append a string at the end of a text file (UTF-8)"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
