##https://leetcode.com/problems/valid-sudoku/

from functools import reduce
from typing import List

def nth_elem(matrix, n):
    """recives a list of lists
    returns a new list with the nth element of each list of the list of lists"""
    new_list = []
    for list in matrix:
        new_list.append(list[n])
    return new_list

def transpose(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        new_matrix.append(nth_elem(matrix, i))
    return new_matrix

def to_boxes(matrix):
    """recives a matrix 9x9 and 
    returns a list of lists where each list is a 3x3 box like in sudoku"""
    boxes = []
    for i in set([0, 3, 6]):
        for j in set([0, 3, 6]):
            new_list = []
            for l in range(3):
                for k in range(3):
                    new_list.append(matrix[i+l][j + k])
            boxes.append(new_list)
    return boxes
    
def isValid(seq):
    """recives a list of 9 elements
    determines if the digits from 1 to 9 are present 0 or 1 times"""
    digits = "123456789"
    used = set()
    for elem in seq:
        if elem in digits:
            if elem in used:
                return False
            else:
                used.add(elem)
    return True

def validRows(matrix):
    are_valid = list(map(lambda x : isValid(x), matrix))
    return reduce (lambda x, y : x and y, are_valid, True)

def validColumns(matrix):
    matrix = transpose(matrix)
    return validRows(matrix)

def validBoxes(matrix):
    matrix = to_boxes(matrix)
    return validRows(matrix)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return validRows(board) and validColumns(board) and validBoxes(board)

