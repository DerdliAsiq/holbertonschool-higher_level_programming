#!/usr/bin/python3
<<<<<<< HEAD
"""Module that defines a function to read and print a text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its contents to stdout."""
=======
"""Read file function."""


def read_file(filename=""):
    """Read file and print."""
>>>>>>> 7158139 (added new repo)
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
