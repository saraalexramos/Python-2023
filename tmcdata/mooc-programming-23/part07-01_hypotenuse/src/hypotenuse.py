'''
Please write a function named hypotenuse(leg1: float, leg2: float), which takes the lengths of the two sides adjacent to the right angle of an orthogonal triangle. 
The function should return the length of the hypotenuse, or the side opposite to the right angle.
'''

import math

def hypotenuse(len1: float, len2: float):
    return math.sqrt(len1 **2 + len2 **2)