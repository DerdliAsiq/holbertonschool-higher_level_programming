#!/usr/bin/python3
<<<<<<< HEAD
"""Module that defines MyList class inheriting from list."""


class MyList(list):
    """Custom list class with a method to print a sorted version."""

    def print_sorted(self):
        """Print the list in ascending sorted order without modifying it."""
=======
"""MyList module."""


class MyList(list):
    """MyList class that inherits from list."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
>>>>>>> 7158139 (added new repo)
        print(sorted(self))
