# Please write a function named list_of_stars, which takes a list of integers as its argument. The function should print out lines of star characters. The numbers in the list specify how many stars each line should contain.

def list_of_stars(list):
    for number in list:
        print(number * "*")