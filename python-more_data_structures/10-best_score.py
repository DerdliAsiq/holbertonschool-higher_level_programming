#!/usr/bin/python3
def best_score(a_dictionary):
<<<<<<< HEAD
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
=======
    if not a_dictionary:
>>>>>>> 7158139 (added new repo)
        return None
    return max(a_dictionary, key=a_dictionary.get)
