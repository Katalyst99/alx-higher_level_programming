#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_e = 0
    try:
        for value in range(0, x):
            print('{:d}'.format(my_list[value]), end='')
            num_e += 1
    except (ValueError, TypeError):
        pass
    finally:
        print('')
        return num_e
