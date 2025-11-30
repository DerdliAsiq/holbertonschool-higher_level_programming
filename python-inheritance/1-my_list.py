#!/usr/bin/python3
"""Module that defines MyList class inheriting from list."""


class MyList(list):
    """Custom list class with a method to print a sorted version."""

    def print_sorted(self):
        """Print the list in ascending sorted order without modifying it."""
        print(sorted(self))
