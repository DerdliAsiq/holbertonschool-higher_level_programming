#!/usr/bin/python3
<<<<<<< HEAD
"""7-rectangle module: defines a Rectangle class with
customizable print symbol and instance counter.
"""


class Rectangle:
    """Class that defines a rectangle by width and height.

    Class Attributes:
        number_of_instances (int): counts the number of Rectangle instances.
        print_symbol: symbol used for string representation (can be any type).
    """
=======
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
>>>>>>> 7158139 (added new repo)

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
<<<<<<< HEAD
        """Initialize a new Rectangle.

        Args:
            width (int): rectangle width (default 0)
            height (int): rectangle height (default 0)
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width."""
=======
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
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
        """Return the string representation of the rectangle.

        Uses the character(s) stored in print_symbol.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        line = symbol * self.__width
        return "\n".join(line for _ in range(self.__height))

    def __repr__(self):
        """Return a string representation that can recreate the instance."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Actions on instance deletion."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
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
            rect.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
>>>>>>> 7158139 (added new repo)
