#!/usr/bin/python3
for a in range(97, 123):
    if chr(a) not in {'e', 'q'}:
        print("{}".format(chr(a)), end="")
