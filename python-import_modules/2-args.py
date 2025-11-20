#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    else:
        print(f"{argc} argument{'' if argc == 1 else 's'}:")
        for i in range(1, argc + 1):
            print(f"{i}: {sys.argv[i]}")
