# Please write a function named row_correct(sudoku: list, row_no: int), which takes a two-dimensional array representing a sudoku grid, and an integer referring to a single row, as its arguments.
# Rows are indexed from 0.

# The function should return True or False, depending on whether the row is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.

def row_correct(sudoku:list, row_no: int):
    alist = [] # a auxiliar list to help -knowing if the number is repeated or not
    
    # to run all the number in the list
    for number in sudoku[row_no]: 
        if number == 0:
            continue # if number = 0 the program will ignore it, and procced to the next number
        elif number not in alist:
            alist.append(number) # if number is not in alist it will add it
        elif number in alist:
            return False # is the number already on the list (is repeated), it will return False
    return True #otherwise it will return True
