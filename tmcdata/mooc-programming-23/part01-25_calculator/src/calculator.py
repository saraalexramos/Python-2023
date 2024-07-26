num1 = int(input(print("")))
num2 = int(input(print("")))
operation = input(print(""))

condition = operation == "add"
if condition:
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

condition = operation == "multiply"
if condition:
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

condition = operation == "subtract"
if condition:
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")