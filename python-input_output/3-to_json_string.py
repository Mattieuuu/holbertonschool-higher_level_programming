#!/usr/bin/python3
'''import my object to json file
'''


import json

def to_json_string(my_obj):
    """returns a json representation of an object"""
    return json.dumps(my_obj)
