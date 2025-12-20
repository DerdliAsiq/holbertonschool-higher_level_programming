#!/usr/bin/python3
<<<<<<< HEAD
"""Module that provides a function to serialize an object to a dict."""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization of an object."""
=======
"""Class to JSON module."""


def class_to_json(obj):
    """Return the dictionary description with simple data structure."""
>>>>>>> 7158139 (added new repo)
    return obj.__dict__
