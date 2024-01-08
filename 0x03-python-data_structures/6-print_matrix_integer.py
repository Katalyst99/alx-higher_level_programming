#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num1 in range(len(matrix)):
        for num2 in range(len(matrix[num1])):
                if num2 < len(matrix[num1]) - 1:
                    print('{:d}'.format(matrix[num1][num2]), end='')
                else:
                    print('{:d}'.format(matrix[num1][num2]), end='')
        print('')
