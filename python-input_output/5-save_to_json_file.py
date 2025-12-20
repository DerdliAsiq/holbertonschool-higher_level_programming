#!/usr/bin/python3
<<<<<<< HEAD
"""Module that saves a Python object to a file as JSON."""
=======
"""Save Object to a file module."""
>>>>>>> 7158139 (added new repo)
import json


def save_to_json_file(my_obj, filename):
<<<<<<< HEAD
    """Write an object to a text file using its JSON representation."""
=======
    """Write object to text file using JSON representation."""
>>>>>>> 7158139 (added new repo)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
