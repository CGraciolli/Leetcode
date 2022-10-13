##https://leetcode.com/problems/rotate-image/

def transpose(matrix):
    """
    transposes a matrix
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
def mirror_y(matrix):
    """
    changes the matrix so that it is rotated at the y axis
    """
    for row in matrix:
        row.reverse()


def transpose(matrix):
    transpose(matrix)
    mirror_y(matrix)