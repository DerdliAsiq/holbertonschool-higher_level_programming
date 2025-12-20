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
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
=======
    """Square class inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize the square."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
>>>>>>> 7158139 (added new repo)
