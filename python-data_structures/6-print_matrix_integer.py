#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        n = 0
        for j in i:
            if n == len(i) - 1:
                print("{:d}".format(j), end="")
                n += 1
            else:
                print("{:d}".format(j), end=" ")
                n += 1
        print()
