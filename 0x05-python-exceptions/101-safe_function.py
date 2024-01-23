#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        f_result = fct(*args)
        return f_result
    except Exception as error:
        print('Exception: {}'.format(error), file=sys.stderr)
        return None
