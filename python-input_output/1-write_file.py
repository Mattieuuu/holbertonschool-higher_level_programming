#!/usr/bin/python3
'''write_file
'''


def write_file(filename="", text=""):
    """Write a string to a text file (UTF-8)"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
