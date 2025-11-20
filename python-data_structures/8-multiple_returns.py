#!/usr/bin/python3
def multiple_returns(sentence):
    """Return a tuple with the length of a string and its first character.
    If the sentence is empty, first character is None.
    """
    if sentence is None or len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
