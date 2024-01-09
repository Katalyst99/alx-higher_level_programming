#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        c = ord(letter)
        if c >= 97 and c <= 122:
            c = chr(c) - 32
         print('{:c}'.format(c), end='')
    print()
