#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
<<<<<<< HEAD
    """Replace an element of a list at a specific position.
    If idx is negative or out of range, returns the original list.
    """
=======
>>>>>>> 7158139 (added new repo)
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
