# In this exercise we will complete two more functions for the sudoku project from the previous section: print_sudoku and add_number.

# The function print_sudoku(sudoku: list) takes a two-dimensional array representing a sudoku grid as its argument. 
# The function should print out the grid in the format specified in the examples below.

# The function add_number(sudoku: list, row_no: int, column_no: int, number:int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. 
# The function should add the digit to the specified location in the grid.



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

def add_number(sudoku:list, row_no:int, column_no: int, number:int):
    sudoku[row_no][column_no] = number
    return sudoku



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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)