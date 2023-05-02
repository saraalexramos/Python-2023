# Please write a program which asks the user for a positive integer N. The program then prints out all numbers between -N and N inclusive, but leaves out the number 0. 
# Each number should be printed on a separate line.

limit = int(input("Please type in a positive integer: "))

numbers = range(-limit, limit +1)
for number in numbers:
        if number == 0:
                continue
        print(number)