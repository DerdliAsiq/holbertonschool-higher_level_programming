#!/usr/bin/python3
"""Module that defines a Student class with filtered JSON serialization."""


class Student:
    """Class that defines a student by first_name, last_name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes with names in attrs
        are included (and only if they exist). Otherwise, all attributes
        are returned.
        """
        if isinstance(attrs, list) and all(type(a) is str for a in attrs):
            return {k: getattr(self, k)
                    for k in attrs if hasattr(self, k)}
        return self.__dict__
