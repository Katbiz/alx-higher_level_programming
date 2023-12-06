#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """Class that inherits from list.

    """
    def print_sorted(self):
        """Prints a list in ascending order.
        """
        list_ = self[:]
        list_.sort()
        print(list_)
