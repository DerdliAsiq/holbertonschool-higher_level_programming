#!/usr/bin/python3
<<<<<<< HEAD
"""Module that defines a Student class with filtered JSON serialization."""


class Student:
    """Class that defines a student by first_name, last_name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
=======
"""Student to JSON with filter module."""


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
            return {k: getattr(self, k)
                    for k in attrs if hasattr(self, k)}
=======
        """Return dictionary representation with filter."""
        if (type(attrs) is list and
                all(type(element) is str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
>>>>>>> 7158139 (added new repo)
        return self.__dict__
