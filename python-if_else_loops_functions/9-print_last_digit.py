#!/usr/bin/python3
def print_last_digit(number):
    last = abs(number) % 10
<<<<<<< HEAD
    print(last, end="")
=======
    print("{}".format(last), end="")
>>>>>>> 7158139 (added new repo)
    return last
