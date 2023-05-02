# Please write a function named box_of_hashes, which prints out a rectangle of hash characters. 
# The function takes one argument, which specifies the height of the rectangle. The rectangle should be ten characters wide.

# The function should call the function line from the exercise above for the actual printing out. 
# Copy your solution to that exercise above the code for this exercise. Please don't change anything in your line function.



def line(number:int, string: str):
    if string == "":
        print(number*"*")
    else:
        print(number * string[0])

def box_of_hashes(number):
    i = 1
    
    while i <= number:
        line(10, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
