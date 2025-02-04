#!/usr/bin/python3

class MyList(list):
    ''' This class inherits from list() '''

    def print_sorted(self):
        """ prints the sorted list """
        print(sorted(self))
