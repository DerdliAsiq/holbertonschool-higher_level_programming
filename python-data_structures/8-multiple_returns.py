#!/usr/bin/python3
def multiple_returns(sentence):
<<<<<<< HEAD
    """Return a tuple with the length of a string and its first character.
    If the sentence is empty, first character is None.
    """
    if sentence is None or len(sentence) == 0:
=======
    if len(sentence) == 0:
>>>>>>> 7158139 (added new repo)
        return (0, None)
    return (len(sentence), sentence[0])
