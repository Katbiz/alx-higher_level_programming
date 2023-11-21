#!/usr/bin/python3

def safe_print_integer_err(value):
    """In this function, if safe_print_integer_err(42) successfully prints
    the integer 42, it returns True, and the message "Printing successful!"
    is printed. If there's an error, it returns False, and the
    message "Printing failed. Check stderr for details.
    " is printed, along with the error message written to stderr.

    """
    import sys
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return False
    else:
        return True
