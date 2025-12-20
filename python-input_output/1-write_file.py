#!/usr/bin/python3
<<<<<<< HEAD
"""Module that defines a function to write text to a file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return number of characters.

    Overwrites the file if it exists, creates it otherwise.
    """
=======
"""Write file module."""


def write_file(filename="", text=""):
    """Write string to file."""
>>>>>>> 7158139 (added new repo)
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
