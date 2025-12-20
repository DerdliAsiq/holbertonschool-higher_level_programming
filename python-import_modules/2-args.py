#!/usr/bin/python3
<<<<<<< HEAD
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    else:
        print(f"{argc} argument{'' if argc == 1 else 's'}:")
        for i in range(1, argc + 1):
            print(f"{i}: {sys.argv[i]}")
=======
import sys

if __name__ == "__main__":
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
>>>>>>> 7158139 (added new repo)
