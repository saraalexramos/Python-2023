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

def block_correct(sudoku:list, row_no: int, column_no:int):

    elements_in_block = [] # list to store elements in block 
    x = "" # a helper variable to store True/ False depending if number appear just one time per row, or more  

    for row in sudoku[row_no:(row_no + 3)]:
        for col in row[column_no:(column_no + 3)]:
            elements_in_block.append(col)

    for element in elements_in_block:
        count = elements_in_block.count(element)
        if 1 <= element <= 9:
            if count == 1:
                x = True
            elif count != 1:
                x = False
                break
    return x
        
    
        
    
def sudoku_grid_correct(sudoku:list):
    
    for row in range (9):
        status = row_correct(sudoku, row)
        if status == False:
            print("row false")
            return False

    for col in range (9):
        status = column_correct(sudoku, col)
        if status == False:
            print("col false")
            return False

    indexes = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]

    for index in indexes:
        status= block_correct(sudoku, index[0], index[1])
        if status == False:
            print("index false")
            return False
    
    return True

if __name__ == "__main__":
    sudoku = [
    [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
    [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
    [ 0, 5, 1, 6, 0, 0, 8, 3, 9 ],
    [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
    [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
    [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
    [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
    [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
    [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]
    x = sudoku_grid_correct(sudoku)
    print(x)