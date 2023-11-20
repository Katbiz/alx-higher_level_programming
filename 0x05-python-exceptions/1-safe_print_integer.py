#!/usr/bin/python3

def safe_print_integer(value):

    """
    Prints an integer with "{:d}".format().
    You have to use try: / except:
    You have to use "{:d}".format() to print as integer you
    are not allowed to import any module
    You are not allowed to use type()

    """
            try:
                        print("{:d}".format(value))
            except (ValueError, TypeError):
                        return False
            else:
                        return True
