#!/usr/bin/python3
<<<<<<< HEAD
"""Module that creates an object from a JSON file."""
=======
"""Load from JSON file module."""
>>>>>>> 7158139 (added new repo)
import json


def load_from_json_file(filename):
<<<<<<< HEAD
    """Create and return a Python object from a JSON file."""
=======
    """Create object from a JSON file."""
>>>>>>> 7158139 (added new repo)
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
