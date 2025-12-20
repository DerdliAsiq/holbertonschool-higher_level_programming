#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
<<<<<<< HEAD
    """Print all integers of a list in reverse order, one per line"""
    if my_list is None:
        return
    for number in my_list[::-1]:
        print("{:d}".format(number))
=======
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
>>>>>>> 7158139 (added new repo)
