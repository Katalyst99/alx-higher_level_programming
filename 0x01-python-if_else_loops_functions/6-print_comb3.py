#!/usr/bin/python3
for digit1 in range(0, 9):
    for digit2 in range(digit1 + 1, 10):
        if f"{digit1}{digit2}" == "89":
            print(f"{digit1}{digit2}")
        else:
            print(f"{digit1}{digit2}", end=", ")
