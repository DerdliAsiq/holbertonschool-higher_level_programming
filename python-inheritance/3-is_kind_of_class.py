#!/usr/bin/python3
<<<<<<< HEAD
"""Module that checks if an object is an instance of a class or its subclass."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclass.

    Otherwise, return False.
    """
=======
"""Same class or inherit from."""


def is_kind_of_class(obj, a_class):
    """Check if object is instance or inherited."""
>>>>>>> 7158139 (added new repo)
    return isinstance(obj, a_class)
