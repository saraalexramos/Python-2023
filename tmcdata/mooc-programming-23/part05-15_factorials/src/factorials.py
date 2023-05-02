# Please write a function named factorials(n: int), which returns the factorials of the numbers 1 to n in a dictionary. The number is the key, and the factorial of that number is the value mapped to it.


def factorials(n: int):
    
    factorials_dict = {} # a dictionary to keep n as keys and the factorial of n as values

    while n > 0: # while the number is major than 0 (since the n is decreasing per iteration)
        x = n
        factorial = 1 # avariable to keep temporarly the factorial of a number

        while x > 0: #to run all the numbers from the end to start 
            factorial *= x # and multiply that number to the factorial value
            x -= 1

        factorials_dict[n]= factorial # add the keys and values to the factorials_dict

        n -= 1

    return factorials_dict

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])