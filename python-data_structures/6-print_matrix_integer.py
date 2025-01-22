#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # Iterate over each row in the matrix
    for row in matrix:
        # Iterate over each element in the row
        for i in range(len(row)):
            # Print the current element formatted as an integer
            print("{:d}".format(row[i]), end="")
            # If it's not the last element, print a space
            if i < len(row) - 1:
                print(" ", end="")
        # Print a new line after each row of the matrix
        print()
