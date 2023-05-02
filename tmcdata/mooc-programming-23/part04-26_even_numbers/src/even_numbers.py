# Please write a function named even_numbers, which takes a list of integers as an argument. The function returns a new list containing the even numbers from the original list.

def even_numbers(list):
    list_even= []
    for number in list:
        if number % 2 == 0:
            list_even.append(number)
        else:
            continue
    return list_even