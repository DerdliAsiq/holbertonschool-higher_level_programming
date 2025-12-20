#!/usr/bin/python3
def safe_print_division(a, b):
<<<<<<< HEAD
    result=None
    try:
        result=a/b
    except Exception:
        result=None
=======
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
>>>>>>> 7158139 (added new repo)
    finally:
        print("Inside result: {}".format(result))
    return result
