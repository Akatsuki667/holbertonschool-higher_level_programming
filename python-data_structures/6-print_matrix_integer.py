#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    j = 0
    for i in matrix:
        for j in i:
            print("{:d} ".format(j), end=" ")
        print("\n")
