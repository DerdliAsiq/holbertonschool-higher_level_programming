#!/usr/bin/python3
def uppercase(str):
    for c in str:
<<<<<<< HEAD
        code = ord(c)
        if 97 <= code <= 122:
            c = chr(code - 32)
        print("{}".format(c), end="")
    print("")
=======
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print()
>>>>>>> 7158139 (added new repo)
