#!/usr/bin/python3
def no_c(my_string):
    """Return a new string with all 'c' and 'C' characters removed."""
    result = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            result += ch
    return result
