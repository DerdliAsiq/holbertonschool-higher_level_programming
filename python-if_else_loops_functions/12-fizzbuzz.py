#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
<<<<<<< HEAD
        if i % 15 == 0:
=======
        if i % 3 == 0 and i % 5 == 0:
>>>>>>> 7158139 (added new repo)
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
<<<<<<< HEAD
            print(i, end=" ")
=======
            print("{}".format(i), end=" ")
>>>>>>> 7158139 (added new repo)
