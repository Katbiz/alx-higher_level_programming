#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    
    for interger in my_list:
        my_list.reverse()
        print("{:d}".format(interger))
