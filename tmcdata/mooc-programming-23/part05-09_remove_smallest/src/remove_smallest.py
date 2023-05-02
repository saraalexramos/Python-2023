# Please write a function named remove_smallest(numbers: list), which takes a list of integers as its argument.

# The functions should find and remove the smallest item in the list. You may assume there is a single smallest item in the list.
#The function should not have a return value - it should directly modify the list it receives as a parameter.


def remove_smallest(numbers:list):
    smallest = max(numbers) # a variable to contain the smallest number
    for number in numbers: # to run al the numbers within the list "numbers"
        if number < smallest: 
            smallest = number # if the number is small than "smallest" it will replace it in the variable
        elif number >= smallest:
            continue # if not (previous commentary) the program will continue to the next number
    numbers.remove(smallest) # at the end we will remove the smallest number from the list
