#!/usr/bin/python3
def element_at(my_list, idx):
<<<<<<< HEAD
    """Retrieve an element from a list at a given index.
    Returns None if index is negative or out of range.
    """
=======
>>>>>>> 7158139 (added new repo)
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
