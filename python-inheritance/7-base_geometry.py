#!/usr/bin/python3
<<<<<<< HEAD
"""Module that defines BaseGeometry with validation helpers."""
=======
"""BaseGeometry module."""
>>>>>>> 7158139 (added new repo)


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
<<<<<<< HEAD
        """Raise exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): name of the parameter.
            value (int): value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
=======
        """Raise exception for area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
>>>>>>> 7158139 (added new repo)
