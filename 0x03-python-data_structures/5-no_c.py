#!/usr/bin/python3
def no_c(my_string):
    newstring = ''
    for ch in range(len(my_string)):
        if my_string[ch] != 'c' and my_string[ch] != 'C':
            newstring += my_string[ch]
    return newstring
