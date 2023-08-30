#!/usr/bin/python3

def safe_print_division(a, b):
    """
    It divides 2 integers and prints the result.
    
    GUIDE
    1. You have to use try: / except:
    2. You have to use "{:d}".format() to print the result.
    3. The result of the division should print on the finally: section,
    preceded by Inside result:
    4. You are not allowed to import any module

        Args:
            a: Integer
            b: Integer

        Returns: The value of the division, otherwise: None
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
