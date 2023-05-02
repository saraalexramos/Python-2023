# Please write a function named spruce, which takes one argument. The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.

def spruce(lines):
    limit = lines * 2 - 1 # the lenght of the 2nd to last line
    print("a spruce!")
    i = 1
    while i <= limit:
        spaces = (limit -i)//2
        print(spaces * " ", end = "")
        print(i * "*", end = "")
        print(spaces * " ", end = "")
        print()

        i += 2

    spaces = (limit -1)//2
    print(spaces * " ", end = "")
    print("*", end = "")
    print(spaces * " ", end = "")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)