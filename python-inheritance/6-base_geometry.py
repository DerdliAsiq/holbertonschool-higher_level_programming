#!/usr/bin/python3
"""Module that defines BaseGeometry class with unimplemented area()."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise exception because area is not implemented."""
        raise Exception("area() is not implemented")
