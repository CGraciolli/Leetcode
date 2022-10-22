##https://leetcode.com/problems/set-matrix-zeroes/

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroes.append([i, j]) 
        for elem in zeroes:
            i = elem[0]
            j = elem[1]
            matrix[i] = [0]*len(matrix[0])
            for k in range(len(matrix)):
                matrix[k][j] = 0