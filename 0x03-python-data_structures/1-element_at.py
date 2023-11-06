#!/usr/bin/python3

def element_at(my_list, idx):

    """ This function retrieves an element in a list,
    if statement is used to evaluate, if less than zero,
    it returns nothing also if idx is longer than length
    it returns nothing again else.
    """

    if my_list:
       if idx < 0:
           return
       elif idx > len(my_list) -1:
           return
       else:
           return my_list[idx]
