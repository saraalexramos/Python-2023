# The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. 
# The function should return a copy of the original grid with the new digit added in the correct location. The function should not change the original grid received as a parameter.


import copy

def print_sudoku(sudoku:list):
    y = 0 # a auxiliar variable to count the number of rows(to make the 3x3 grids in sudoku)
    for row in sudoku:
        x = 0 # a auxiliar variable to count the number of number (to make the 3x3 grids in sudoku)
        for number in row:

            # is the number is 0 it will print a "_"
            if number == 0:
                print("_", end = " ")
            # if the number is not 0 it will print the number
            elif number != 0:
                print(number, end = " ")
            #every 3 columns (or numbers) it will print a space (to make the 3x3 grids in sudoku)
            if x == 2 or x == 5:
                print(" ", end = "")
            x += 1
        print()
        # every 3 rows it will print a line in blank (to make the 3x3 grids in sudoku)
        if y == 2 or y == 5:
            print()
        y += 1


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku_copy = copy.deepcopy(sudoku)
    sudoku_copy[row_no][column_no]= number
    return sudoku_copy




if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
