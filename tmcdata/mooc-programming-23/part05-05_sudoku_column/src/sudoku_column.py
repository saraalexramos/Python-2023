# The function should return True or False, depending on whether the column is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.

def column_correct(sudoku: list, column_no: int):
    alist = [] # an auxiliar list to help find the repeated numbers
    for row in sudoku: # to run all the rows in sudoku
        if row[column_no] == 0:
            continue # if the number is equal 0 it will proceed, and ignore it
        elif row[column_no]  not in alist:
            alist.append(row[column_no]) # if the number is not in alist, it will add it 
        elif row[column_no]  in alist: 
            return False #if the number already in list (it means is repeated), so it will return False
    return True
