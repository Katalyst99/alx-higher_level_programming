#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_e = 0
    try:
        for value in range(x):
            print(my_list[value], end="")
            num_e += 1
    except IndexError:
        pass
    finally:
        print('')
        return num_e
