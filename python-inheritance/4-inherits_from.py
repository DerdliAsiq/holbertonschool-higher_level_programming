#!/usr/bin/python3
<<<<<<< HEAD
"""Module that checks for *strict* inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    The object's type must be a subclass (directly or indirectly) of a_class,
    but not a_class itself.
    """
=======
"""Only sub class of."""


def inherits_from(obj, a_class):
    """Check if object inherits from a_class."""
>>>>>>> 7158139 (added new repo)
    return isinstance(obj, a_class) and type(obj) is not a_class
