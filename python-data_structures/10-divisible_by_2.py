#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Return a list of booleans indicating if elements are divisible by 2."""
    result = []
    for number in my_list:
        result.append(number % 2 == 0)
    return result
