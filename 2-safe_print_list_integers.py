#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    It prints the first x elements of a list and only integers.
   
    GUIDE
    1. my_list can contain any type (integer, string, etc.)
    2. You have to use try: / except:
    3. You have to use "{:d}".format() to print as integer.
    4. You are not allowed to import any module.
    5.  All integers have to be printed on the same line followed by a new line,
    - other type of value in the list must be skipped (in silence).
    6. You are not allowed to use len().

        Args:
            x: Number of elements to access in my_list.

        Returns: The real number of integers printed.
    """
    count = 0
    for item in range(x):
        if isinstance(my_list[item], int):
            try:
                print(my_list[item], end='')
            except IndexError:
                break
        else:
            continue
        count += 1
    print()
    return count
