#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    """
    This function aims to print out the first x elements of the the list  my_list.
"""
    count = 0
    for item in range(x):
        if isinstance(my_list[item], int):
            try:
                print(my_list[itme], end='')
            except IndexError:
                break
            else:
                count += 1
        else:
            continue
    print()
    return count
