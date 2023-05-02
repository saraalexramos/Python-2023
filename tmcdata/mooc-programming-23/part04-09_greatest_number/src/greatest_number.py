# Please write a function named greatest_number, which takes three arguments. The function returns the greatest in value of the three.

def greatest_number(num1, num2, num3):
    numbers = []
    numbers.append(num1)
    numbers.append(num2)
    numbers.append(num3)

    return max(numbers)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)