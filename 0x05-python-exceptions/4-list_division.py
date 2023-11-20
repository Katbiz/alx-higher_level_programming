#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    """
    The function returns the new_list containing all the results of the divisions.
    This function is designed to handle different types of exceptions during
    element-wise division of two lists and to provide meaningful error messages.
    The result of each division (or 0 in case of an exception)
    is appended to a new list, which is then returned.
"""
new_list = []

for item in range(list_length):
    try:
        quotient = my_list_1[item] / my_list_2[item]
    except IndexError:
        print("Out of range")
    except TypeError:
        print("Wrong type")
    except ZeroDivisionError:
        print("division by 0")

        quotient = 0
    finally:
        new_list.append(quotient)
return new_list
