#!/usr/bin/python3

def raise_exception_msg(message=""):
    """
    In this function, calling raise_exception_msg("This is a custom error message.")
    will raise a NameError with the specified message.
    The except block then catches the exception and prints a
    message indicating that a NameError was caught,
    along with the custom error message.
    """
    raise NameError(message)
