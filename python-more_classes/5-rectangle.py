#!/usr/bin/python3
<<<<<<< HEAD
"""5-rectangle module: defines a Rectangle class with deletion message."""


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
>>>>>>> 7158139 (added new repo)
        self.width = width
        self.height = height

    @property
    def width(self):
<<<<<<< HEAD
        """Retrieve the width."""
=======
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

    def area(self):
<<<<<<< HEAD
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.

        If width or height is 0, return 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the string representation of the rectangle using '#'.

        If width or height is 0, return an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        line = "#" * self.__width
        return "\n".join(line for _ in range(self.__height))

    def __repr__(self):
        """Return a string representation that can recreate the instance."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance is deleted."""
=======
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            rect.append("#" * self.__width)
        return "\n".join(rect)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
>>>>>>> 7158139 (added new repo)
        print("Bye rectangle...")
