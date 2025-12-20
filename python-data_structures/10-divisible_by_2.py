#!/usr/bin/python3
def divisible_by_2(my_list=[]):
<<<<<<< HEAD
    """Return a list of booleans indicating if elements are divisible by 2."""
    result = []
    for number in my_list:
        result.append(number % 2 == 0)
    return result
=======
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
>>>>>>> 7158139 (added new repo)
