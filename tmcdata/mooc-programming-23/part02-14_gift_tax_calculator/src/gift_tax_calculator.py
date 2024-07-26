gift = int(input("Value of gift: "))
if gift < 5000:
    print("No tax!")
else:
    if 5000 <= gift < 25000:
        tax = (100 + (gift - 5000) * 0.08)
    elif 25000 <= gift < 50000:
        tax = (1700 + (gift - 25000) * 0.10)
    elif 55000 <= gift < 200000:
        tax = (4700 + (gift - 55000) * 0.12)
    elif 200000 <= gift < 1000000:
        tax=(22100 + (gift - 200000) * 0.15)
    elif 1000000 <= gift:
        tax = (142100 + (gift - 1000000) * 0.17)
    print(f"Amount of tax: {tax}")