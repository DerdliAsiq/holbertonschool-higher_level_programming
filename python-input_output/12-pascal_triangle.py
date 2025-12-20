#!/usr/bin/python3
<<<<<<< HEAD
"""Module that generates Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of size n.

    Args:
        n (int): number of rows in the triangle.

    Returns:
        list: list of lists of ints; empty list if n <= 0.
    """
=======
"""Pascal's Triangle module."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle."""
>>>>>>> 7158139 (added new repo)
    if n <= 0:
        return []

    triangle = [[1]]
<<<<<<< HEAD

    for _ in range(1, n):
        prev_row = triangle[-1]
        row = [1]
        for i in range(len(prev_row) - 1):
            row.append(prev_row[i] + prev_row[i + 1])
        row.append(1)
        triangle.append(row)

=======
    while len(triangle) != n:
        prev = triangle[-1]
        current = [1]
        for i in range(len(prev) - 1):
            current.append(prev[i] + prev[i + 1])
        current.append(1)
        triangle.append(current)
>>>>>>> 7158139 (added new repo)
    return triangle
