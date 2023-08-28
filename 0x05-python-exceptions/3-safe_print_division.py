#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        anss = a / b
    except (ZeroDivisionError, FloatingPointError):
        anss = None
    finally:
        print("Inside result: {}".format(anss))
    return anss
