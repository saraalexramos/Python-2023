# Please write a function named sum_of_positives, which takes a list of integers as its argument. The function returns the sum of the positive values in the list.

def sum_of_positives(list):
    sum = 0
    for number in list:
        if number >= 0:
            sum += number
        else:
            continue
    return sum