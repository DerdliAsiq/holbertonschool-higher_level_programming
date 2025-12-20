#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
<<<<<<< HEAD
    """Print a matrix of integers."""
    for row in matrix:
        for i, value in enumerate(row):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(value), end="")
=======
    for row in matrix:
        for i in range(len(row)):
            print("{:d}".format(row[i]), end="")
            if i != len(row) - 1:
                print(" ", end="")
>>>>>>> 7158139 (added new repo)
        print()
