#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for n in range(len(matrix[i])):
            if n < len(matrix[i]) - 1:
                print('{:d}'.format(matrix[i][n]), end=' ')
            else:
                 print('{:d}'.format(matrix[i][n]), end='')
        print('')
