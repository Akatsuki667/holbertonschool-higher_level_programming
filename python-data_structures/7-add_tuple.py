#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    a, b = tuple_a[:2]
    c, d = tuple_b[:2]

    new_tuple = (a + c, b + d)

    return new_tuple
