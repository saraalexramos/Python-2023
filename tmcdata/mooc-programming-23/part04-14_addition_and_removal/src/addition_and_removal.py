# Please write a program which asks the user to choose between addition and removal. 
# Depending on the choice, the program adds an item to or removes an item from the end of a list. 
# The item that is added must always be one greater than the last item in the list. 
# The first item to be added must be 1.

values = []
print("The list is now", values)
i = 1
while True:
    x = input("a(d)d, (r)emove or e(x)it: ")
    if x == "x":
        print("Bye!")
        break

    elif x == "d":
        values.append(i)
        print("The list is now", values)
        i += 1

    elif x == "r":
        values.remove(i-1)
        print("The list is now", values)
        i -= 1

