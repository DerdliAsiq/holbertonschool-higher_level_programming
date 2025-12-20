#!/usr/bin/python3
<<<<<<< HEAD
"""Module that defines a Student class with JSON helpers."""


class Student:
    """Class that defines a student by first_name, last_name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
=======
"""Student to disk and reload module."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student."""
>>>>>>> 7158139 (added new repo)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
<<<<<<< HEAD
        """Return the dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes with names in attrs
        are included (and only if they exist). Otherwise, all attributes
        are returned.
        """
        if isinstance(attrs, list) and all(type(a) is str for a in attrs):
=======
        """Return dictionary representation with filter."""
        if (type(attrs) is list and
                all(type(element) is str for element in attrs)):
>>>>>>> 7158139 (added new repo)
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
<<<<<<< HEAD
        """Replace all attributes of the Student instance from a dictionary."""
=======
        """Replace all attributes of the Student instance."""
>>>>>>> 7158139 (added new repo)
        for key, value in json.items():
            setattr(self, key, value)
