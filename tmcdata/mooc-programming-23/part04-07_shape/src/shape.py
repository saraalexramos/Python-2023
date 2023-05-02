# Please write a function named shape, which takes four arguments. The first two parameters specify a triangle, as above, and the character used to draw it. 
# The first parameter also specifies the width of a rectangle, while the third parameter specifies its height. 
# The fourth parameter specifies the filler character of the rectangle. The function prints first the triangle, and then the rectangle below it.

# The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.


def line(number:int, string: str):
    if string == "":
        print(number*"*")
    else:
        print(number * string[0])

def shape(size:int, string:str, lines:int, string2:str):
    i = 1
    while i <= size:
        line(i, string)
        i += 1
    j = 1
    while j <= lines:
        line(size, string2)
        j += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")