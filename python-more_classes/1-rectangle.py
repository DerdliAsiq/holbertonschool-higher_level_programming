#!/usr/bin/python3
<<<<<<< HEAD
"""1-rectangle module: defines a Rectangle class with width and height."""


class Rectangle:
    """Class that defines a rectangle by width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): rectangle width (default 0)
            height (int): rectangle height (default 0)
        """
=======
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""
>>>>>>> 7158139 (added new repo)
        self.width = width
        self.height = height

    @property
    def width(self):
<<<<<<< HEAD
        """Retrieve the width."""
=======
        """Get/set the width of the rectangle."""
>>>>>>> 7158139 (added new repo)
        return self.__width

    @width.setter
    def width(self, value):
<<<<<<< HEAD
        """Set the width with validation."""
=======
>>>>>>> 7158139 (added new repo)
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
<<<<<<< HEAD
        """Retrieve the height."""
=======
        """Get/set the height of the rectangle."""
>>>>>>> 7158139 (added new repo)
        return self.__height

    @height.setter
    def height(self, value):
<<<<<<< HEAD
        """Set the height with validation."""
=======
>>>>>>> 7158139 (added new repo)
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
