#!/usr/bin/python3

def multiple_returns(sentence):
    # Return a tuple containing the length of sentence and its first character
    return len(sentence), sentence[0] if sentence else None
