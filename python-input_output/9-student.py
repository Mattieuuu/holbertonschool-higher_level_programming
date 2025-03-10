#!/usr/bin/python3
'''model_class_student
'''


class Student:
    """ Student class with public instance"""

    def __init__(self, first_name, last_name, age):
        """ Initialize the instance with first_name, last_name, and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Return the dictionary representation of the instance """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
