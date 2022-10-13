##https://leetcode.com/problems/spiral-matrix/

from functools import reduce

def is_matrix_empty(matrix):
    """
    returns True if the matrix contains only empty lists
    """
    are_empty = list(map(lambda x: x == [],matrix))
    return reduce(lambda x, y: x and y, are_empty, True)

def spiral_outter_layer(matrix):
    """
    recives a matrix
    returns a list with the elements in the outter layer of the matrix in spiral order
    and the matrix without the outter layer
    """
    ##extreme cases
    if is_matrix_empty(matrix):
        return [], [[]]
    if len(matrix) == 1:
        return matrix[0], [[]]
    elif len(matrix[0]) == 1:
        spiral = []
        for i in range(len(matrix)):
            spiral.append(matrix[i][0])
        return spiral, [[]]
    ##general case
    spiral = []
    ##puts the upper row in spiral
    spiral += matrix[0]
    ##puts the last column in spiral
    for i in range(1, len(matrix) -1):
        spiral.append(matrix[i][-1])
    ##puts the last row in spiral
    i = len(matrix) - 1
    last_row = matrix[i]
    reversed_last_row = last_row[::-1]
    spiral += reversed_last_row
    ##puts the first column in spiral
    for i in range(len(matrix) -2, 0, -1):
        spiral.append(matrix[i][0])
    ##removes the outter layer of the matrix
    ##first we remove tha first and last rows
    matrix = matrix[1:len(matrix) - 1]
    ##then the first and last columns
    if not is_matrix_empty(matrix):
        for i in range(len(matrix)):
            matrix[i] = matrix[i][1:len(matrix[i])-1]
    return spiral, matrix

def spiralOrder(matrix):
        spiral = []
        while matrix != [[]]:
            new_spiral, matrix = spiral_outter_layer(matrix)
            spiral += new_spiral
        return spiral