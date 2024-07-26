'''
Please familiarize yourself with the Python module fractions. 
Use it to write a function named fractionate(amount: int), which takes the number of parts as its argument. 
The function should divide the number 1 into as many equal sized fractions as is specified by the argument, and return these in a list.
'''

import fractions

def fractionate(amount: int):
    fractions_list = []
    i = 1
    while i <= amount:
        fractions_list.append(fractions.Fraction(1, amount))
        i += 1
    return fractions_list

