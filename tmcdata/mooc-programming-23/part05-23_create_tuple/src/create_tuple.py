# Please write a function named create_tuple(x: int, y: int, z: int), which takes three integers as its arguments, and creates and returns a tuple based on the following criteria:

#    The first element in the tuple is the smallest of the arguments
#    The second element in the tuple is the greatest of the arguments
#    The third element in the tuple is the sum of the arguments


def create_tuple(x: int, y: int, z: int):

    values = [] # to store the values in arguments
    values.append(x)
    values.append(y)
    values.append(z)

    # cicle for to rull all values and sum them
    sum = 0
    for value in values:
        sum += value
    
    tuple = (min(values), max(values), sum)
    return tuple