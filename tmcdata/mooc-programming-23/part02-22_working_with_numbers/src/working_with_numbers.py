print("Please type in integer numbers. Type in 0 to finish.")
attempts = 0
sum = 0
positives = 0
negatives = 0

while True:
    num = int(input("Number: "))
    if num > 0:
        positives += 1
    if num < 0:
        negatives += 1
    elif num == 0:
        break
    attempts += 1
    sum += num
    mean = sum / attempts
    

print(f"Numbers typed in {attempts}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {negatives}")
