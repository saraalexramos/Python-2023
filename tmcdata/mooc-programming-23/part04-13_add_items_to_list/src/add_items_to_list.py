# Please write a program which first asks the user for the number of items to be added. 
# Then the program should ask for the given number of values, one by one, and add them to a list in the order they were typed in. Finally, the list is printed out.

items = int(input("How many times: "))
numbers = []
i = 1
while i <= items:
    item = int(input(f"Item {i}: "))
    numbers.append(item)
    i += 1
print(numbers)