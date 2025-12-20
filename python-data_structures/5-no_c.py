#!/usr/bin/python3
def no_c(my_string):
<<<<<<< HEAD
    """Return a new string with all 'c' and 'C' characters removed."""
    result = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            result += ch
    return result
=======
    new_string = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            new_string += i
    return new_string
>>>>>>> 7158139 (added new repo)
