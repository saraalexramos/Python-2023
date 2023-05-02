# Please write a function named square_of_hashes, which draws a square of hash characters. 
# The function takes one argument, which determines the length of the side of the square.

# The function should call the function line from the exercise above for the actual printing out. 
# Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.


def line(number:int, string: str):
    if string == "":
        print(number*"*")
    else:
        print(number * string[0])


def square_of_hashes(size):
    i = 1

    while i <= size:
        line(size, "#")
        i += 1


if __name__ == "__main__":
    square_of_hashes(5)
