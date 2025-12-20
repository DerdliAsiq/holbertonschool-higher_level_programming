#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
<<<<<<< HEAD
    count=0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count+=1
        except Exception:
            break
    print()
    return count
=======
    c = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            c += 1
        except IndexError:
            break
    print("")
    return c
>>>>>>> 7158139 (added new repo)
