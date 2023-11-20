#!/usr/bin/python3

def safe_print_division(a, b):

   """"
   This function is designed to safely perform the division of two integers,
   handling the case where the denominator is zero.
   The use of try/except allows the function to gracefully handle errors,
   and the result is printed in the finally block, ensuring that the message is always displayed.
   The function then returns the result of the division or None in case of a division by zero.
"""

   try:
       result = a / b

   except ZeroDevisioError:
       result = None
   finally:
       print("Inside result: {}".format(result))
    return result
