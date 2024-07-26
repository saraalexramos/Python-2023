# Please write a function named dict_of_numbers(), which returns a new dictionary. The dictionary should have the numbers from 0 to 99 as its keys.
# The value attached to each key should be the number spelled out in words.
'''
numbers = dict_of_numbers()
print(numbers[2])
print(numbers[11])
print(numbers[45])
print(numbers[99])
print(numbers[0])

two
eleven
forty-five
ninety-nine
zero


'''


def dict_of_numbers():
    numbers_dict = {} # the dictionary
    name_numb_19 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    name_numb_unit = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    x = 0 # auxiliar variable for the cicle

    # a cicle while to run all numbers between 0 and 99:
    while x <= 99:

        if x <= 19:
            numbers_dict[x] = name_numb_19[x]
        
        else: # numbers > = 20:
            number1 = x//10 # number 1 is the first digit of the number, for that We nedd to divide the number to 10, and select only the int number
            number2 = x-(number1*10) # the second digit

            if number2 != 0:
                numbers_dict[x] = name_numb_unit[(number1 - 2)] + "-" + name_numb_19[number2]

            else: # number2 == 0:
                numbers_dict[x] = name_numb_unit[(number1 - 2)]

        x += 1 # increase the variable to each iteration, to be a finite loop
    
    return numbers_dict

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[20])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])