#!/usr/bin/python3
<<<<<<< HEAD
"""Module that defines a Student class."""


class Student:
    """Class that defines a student by first_name, last_name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
=======
"""Student to JSON module."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student."""
>>>>>>> 7158139 (added new repo)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
<<<<<<< HEAD
        """Return the dictionary representation of the Student instance."""
=======
        """Return the dictionary representation of a Student instance."""
>>>>>>> 7158139 (added new repo)
        return self.__dict__
