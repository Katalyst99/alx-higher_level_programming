#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a/b
    except (ZeroDivisionError, TypeError, ValueError):
        pass
    finally:
        if result is not None:
            print('Inside result: {}'.format(result))
    return result
