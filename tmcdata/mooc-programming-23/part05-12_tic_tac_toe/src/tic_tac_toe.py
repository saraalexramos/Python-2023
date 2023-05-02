'''
Tic-Tac-Toe is played on a 3 by 3 grid, by two players who take turns inputting noughts and crosses. If either player succeeds in placing three of their own symbols on any row, column or diagonal, they win. If neither player manages this, it is a draw.
Please write a function named play_turn(game_board: list, x: int, y: int, piece: str), which places the given symbol at the given coordinates on the board. The values of the coordinates on the board are between 0 and 2.
The board consists of the following strings:

    "": empty square
    "X": player 1 symbol
    "O": player 2 symbol
The function should return True if the square was empty and the symbol was successfully placed on the game board. The function should return False if the square was occupied, or if the coordinates weren't valid.

'''


def play_turn(game_board:list, x: int , y: int, piece: str):
    # to verify if the coordinates are valid:
    if 0 <= x <= 2 and 0 <= y <= 2:
        # to verify if the block is not occupied:
        if game_board[y][x] == "":
            game_board[y][x] = piece # replace the block with the piece present in the function
            return True
    # if it not meet the conditions above:
    return False

