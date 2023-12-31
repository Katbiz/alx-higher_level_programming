#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Write a function that prints x elements of a list.
    Prototype: def safe_print_list(my_list=[], x=0):
    > my_list can contain any type (integer, string, etc.)
    > All elements must be printed on the same line followed by a new line.
    > x represents the number of elements to print
    > x can be bigger than the length of my_list
    > Returns the real number of elements printed
    > You have to use try: / except:
    > You are not allowed to import any thing
    Approach to project
    write the function protype - define it
    The function takes two parameters my_list[] which is an empty list and
    x which is the number of elements to be printed from the list.
    We start by tracking the number of elements from zero before we start
    printing. by initializing the count function.
    We are going to iterate through the range of x.
    using the for loop. for item in range x
    We then try print my list through items in range x 
    Because we are tring to print out of range,
    we can therefor expect a indexError. 
    to handle the index error the program should break if it
    encounters an IndexError. if not an else statement should take over 
    """
                count = 0
                    for item in range(x):
                                try:
                                                print(my_list[item], end='')
                                except IndexError:
                                                break
                                else:
                                      count += 1
                     print()
                     return count
