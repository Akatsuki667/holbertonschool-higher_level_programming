#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for a in my_string:
        if a not in {'c', 'C'}:
            result += a
    return result
