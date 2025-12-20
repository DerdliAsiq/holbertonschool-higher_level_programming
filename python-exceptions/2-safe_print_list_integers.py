#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
<<<<<<< HEAD
        except (TypeError, ValueError):
            continue
        except IndexError:
            break
    print()
=======
        except (ValueError, TypeError):
            pass
    print("")
>>>>>>> 7158139 (added new repo)
    return count
