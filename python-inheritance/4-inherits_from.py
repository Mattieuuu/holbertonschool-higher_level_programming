#!/usr/bin/python3

def inherits_from(obj, a_class):
    """Check if the object is an instance of a class inherited from specified class"""
    if type(obj) is not a_class:
        return isinstance(obj, a_class)
    return False
