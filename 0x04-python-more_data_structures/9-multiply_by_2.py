#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    m_keys = list(a_dictionary.keys())
    for k in m_keys:
        new_dict[k]= a_dictionary[k] * 2
    return new_dict
