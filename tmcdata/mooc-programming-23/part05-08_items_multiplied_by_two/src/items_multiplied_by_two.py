# Please write a function named double_items(numbers: list), which takes a list of integers as its argument.

# The function should return a new list, which contains all values from the original list doubled. The function should not change the original list.

def double_items(numbers:list):
    a_list = [] # a auxiliar list to be the returned list
    for number in numbers:
        a_list.append(number*2) # run all the numbers and add the doubled number to the a_list
    return a_list