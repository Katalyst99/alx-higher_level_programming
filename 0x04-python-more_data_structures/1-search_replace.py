#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for value in range(len(my_list)):
        if new_list[value] == search:
            new_list[value] = replace
    return new_list
