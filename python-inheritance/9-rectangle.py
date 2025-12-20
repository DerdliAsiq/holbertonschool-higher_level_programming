#!/usr/bin/python3
<<<<<<< HEAD
"""Module that defines a Rectangle class inheriting from BaseGeometry."""
=======
"""Rectangle module."""
>>>>>>> 7158139 (added new repo)
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
<<<<<<< HEAD
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize Rectangle with validated private width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
=======
    """Rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize the rectangle."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
>>>>>>> 7158139 (added new repo)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
<<<<<<< HEAD
        """Return the rectangle description."""
=======
        """Return the string representation of the rectangle."""
>>>>>>> 7158139 (added new repo)
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
