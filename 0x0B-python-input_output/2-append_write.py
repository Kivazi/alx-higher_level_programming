#!/usr/bin/python3
"""Defines a file-writing function."""


def append_write(filename="", text=""):
    """Append a string to a UTF8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
