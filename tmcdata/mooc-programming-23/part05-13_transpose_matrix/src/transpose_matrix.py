# Please write a function named transpose(matrix: list), which takes a two-dimensional integer array, i.e., a matrix, as its argument. The function should transpose the matrix. 
# Transposing means essentially flipping the matrix over its diagonal: columns become rows, and rows become columns.
# You may assume the matrix is a square matrix, so it will have an equal number of rows and columns.


import copy

def transpose(matrix: list):
    matrix_copy = copy.deepcopy(matrix)

    x = 0 # a auxiliar variable to run all the rows in matrix
    while x < len(matrix[0]):
        y = 0 # a auxiliar variable to run all the numbers in matrix
        while y < len(matrix[0]):
            matrix[y][x] = matrix_copy[x][y] # to change the numbers in matrix depending on the matrix_copy
            y += 1 # to increment 1, making the auxiliar variable to change
        x += 1 # to increment 1, making the auxiliar variable to change
    

if __name__ == "__main__":
    matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    x = transpose(matrix)
    print(x)

