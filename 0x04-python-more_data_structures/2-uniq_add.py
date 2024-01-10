#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for value in set(my_list):
        result = result + value
    return result
