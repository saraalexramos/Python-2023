'''
Please write a function named lottery_numbers(amount: int, lower: int, upper: int), which generates as many random numbers as specified by the first argument. 
All numbers should fall within the bounds lower to upper. The numbers should be stored in a list and returned. 
The numbers should be in ascending order in the returned list.

As these are lottery numbers, no number should appear twice in the list.

'''
from random import randint

def lottery_numbers(amount: int, lower: int, upper: int):
    numbers = []
    while len(numbers) < amount:
        x = randint(lower, upper + 1)
        if x in numbers: 
            continue
        else:
            numbers.append(x)
    numbers.sort()
    return numbers