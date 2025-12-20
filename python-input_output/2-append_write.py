#!/usr/bin/python3
<<<<<<< HEAD
"""Module that defines a function to append text to a file."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file and return characters added.

    Creates the file if it does not exist.
    """
=======
"""Append write module."""


def append_write(filename="", text=""):
    """Append string to file."""
>>>>>>> 7158139 (added new repo)
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
