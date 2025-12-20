#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
<<<<<<< HEAD
    except Exception:
=======
    except (ValueError, TypeError):
>>>>>>> 7158139 (added new repo)
        return False
