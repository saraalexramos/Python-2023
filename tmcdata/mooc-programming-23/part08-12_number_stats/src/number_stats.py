# Please write a class named NumberStats with the following methods:

#    the method add_number adds a new number to the statistical record
#    the method count_numbers returns the count of how many numbers have been added


# Please add the following methods to your class definition:

    # the method get_sum should return the sum of the numbers added (if no numbers have been added, the method should return 0)
    # the method average should return the mean of the numbers added (if no numbers have been added, the method should return 0)


class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0
        self.sum = 0

    def add_number(self, number:int):
        self.count += 1
        self.sum += number
        pass

    def count_numbers(self):
        return self.count
    
    def get_sum(self):
        return self.sum
    
    def average(self):
        if self.count > 0:
            return self.sum / self.count
        else:
            return 0


# Please write a main program which keeps asking the user for integer numbers until the user types in -1. 
# The program should then print out the sum and the mean of the numbers typed in.
# Your program should use a NumberStats object to keep a record of the numbers added.

# Please add to your main program so that it also counts separately the sum of the even and the odd numbers added.

# NB: do not change your NumberStats class definition in this part of exercise, either. Instead, define three NumberStats objects. 
# One of them should keep track of all the numbers, another should track the even numbers, and the third should track the odd numbers typed in.


stats = NumberStats()
stats_even = NumberStats()
stats_odd = NumberStats()

while True:
    number = int(input("Please type in integer numbers: "))
    # condition to stop the cicle (user types in -1)
    if number == -1:
        print("Sum of numbers:", stats.get_sum())
        print("Mean of numbers:", stats.average())
        print("Sum of even numbers:", stats_even.get_sum())
        print("Sum of odd numbers:", stats_odd.get_sum())
        break
    
    else:
        stats.add_number(number)
        if number % 2 == 0: # if the number is even
            stats_even.add_number(number)
        else: # number is odd
            stats_odd.add_number(number)


