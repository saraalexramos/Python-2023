# Please write a function named formatted, which takes a list of floating point numbers as its argument. 
# The function returns a new list, which contains each element of the original list in string format, rounded to two decimal points. The order of the items in the list should remain unchanged.

def formatted(list):
    formatted_list = []
    for number in list:
        formatted_list.append(f"{number:.2f}")
    return formatted_list


