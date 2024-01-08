#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n1 in range(len(matrix)):
        for n2 in range(len(matrix[n1])):
                if n2 < len(matrix[n1]) - 1:
                    print('{:d}'.format(matrix[n1][n2]), end=' ')
                else:
                    print('{:d}'.format(matrix[n1][n2]), end='')
        print('')
