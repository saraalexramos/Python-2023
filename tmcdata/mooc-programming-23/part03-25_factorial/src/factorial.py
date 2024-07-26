

while True:
    num = int(input("Please type in a number: "))
    if num <= 0:
        print("Thanks and bye!")
        break
    res = 1
    i = 1
    while i <= num:
        res *=i
        i+=1
    print(f"The factorial of the number {num} is {res}")
