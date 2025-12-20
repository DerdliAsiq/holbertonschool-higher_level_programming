#!/usr/bin/python3
<<<<<<< HEAD
"""Module that checks if an object is exactly an instance of a given class."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, otherwise False."""
=======
"""Exact same object."""


def is_same_class(obj, a_class):
    """Check if object is exactly an instance of the specified class."""
>>>>>>> 7158139 (added new repo)
    return type(obj) is a_class
