#!/usr/bin/python3
import sys

if __name__ == "__main__":

    arg = len(sys.argv) - 1

    if arg == 0:
        print("0 arguments.")
    elif arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg))
    for i in range(0, arg):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
