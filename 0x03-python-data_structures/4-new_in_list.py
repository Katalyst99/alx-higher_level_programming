#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copylist = my_list
    if idx < 0 or  idx >= len(my_list):
        return copylist
    else:
        copylist[idx] = element
        return copylist
