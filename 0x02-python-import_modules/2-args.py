#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nargs = len(sys.argv[1:])
    if nargs == 0:
        print(f"{nargs} arguments.")
    elif nargs == 1:
        print(f"{nargs} argument:")
    else:
        print(f"{nargs} arguments:")
    for i in range(nargs):
        print('{:d}: {:s}'.format(i + 1, sys.argv[i + 1]))
