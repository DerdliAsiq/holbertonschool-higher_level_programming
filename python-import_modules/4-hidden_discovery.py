#!/usr/bin/python3
<<<<<<< HEAD
if __name__ == "__main__":
    import hidden_4
    for name in dir(hidden_4):
        if not name.startswith("__"):
=======
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
>>>>>>> 7158139 (added new repo)
            print(name)
