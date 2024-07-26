x = 0

while True:
    pin = int(input("PIN: "))
    x += 1
    if pin == 4321:
        if x == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {x} attempts")
        break
    else:
        print("Wrong")

