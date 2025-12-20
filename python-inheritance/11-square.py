#!/usr/bin/python3
<<<<<<< HEAD
"""Module that defines a Square class inheriting from Rectangle."""
=======
"""Square module."""
>>>>>>> 7158139 (added new repo)
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
<<<<<<< HEAD
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize Square with validated private size."""
=======
    """Square class inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize the square."""
>>>>>>> 7158139 (added new repo)
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
<<<<<<< HEAD
        return self.__size * self.__size

    def __str__(self):
        """Return the square description."""
=======
        return self.__size ** 2

    def __str__(self):
        """Return the string representation of the square."""
>>>>>>> 7158139 (added new repo)
        return "[Square] {}/{}".format(self.__size, self.__size)
