# In a game of Go two players take turns to place black and white stones on a game board. 
# The winner is the player who manages to encircle a bigger area on the board with their own game pieces.
# Please write a function named who_won(game_board: list), which takes a two-dimensional array as its argument. 
# The array consists of integer values, which represent the following situations:
#    0: empty square
#    1: player 1 game piece
#    2: player 2 game piece



def who_won(game_board: list):
    count1 = 0
    count2 = 0
    for row in game_board:
        for number in row:
            if number == 1:
                count1 += 1
            elif number == 2:
                count2 += 1
            
    if count1 > count2:
        return 1
    elif count2 > count1:
        return 2
    return 0
