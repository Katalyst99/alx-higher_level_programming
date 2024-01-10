#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order_keys = sorted(a_dictionary)
    for k in order_keys:
        print("{:s}: {}".format(k, a_dictionary[k]))
