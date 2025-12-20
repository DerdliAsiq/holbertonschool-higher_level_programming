#!/usr/bin/python3
def max_integer(my_list=[]):
<<<<<<< HEAD
    """Return the biggest integer of a list.
    If the list is empty, return None.
    """
    if not my_list:
        return None
    max_val = my_list[0]
    for number in my_list[1:]:
        if number > max_val:
            max_val = number
    return max_val
=======
    if len(my_list) == 0:
        return None

    biggest = my_list[0]
    for i in my_list:
        if i > biggest:
            biggest = i

    return biggest
>>>>>>> 7158139 (added new repo)
