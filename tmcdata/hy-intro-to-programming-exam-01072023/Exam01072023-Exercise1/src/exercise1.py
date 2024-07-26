result = 0
print(result)

while True:
    operation = input("Type in a calculation or quit: ")
    if operation.lower() == "quit":
        break

    # split the two parts of the operation input
    operator = operation[0]
    number = int(operation[1:])

    match operator:
        case "-": # subtration
            result -= number
        case "+": # sum
            result += number
        case "/": # divition
            result /= number
        case "*": # multiplication
            result *= number

    print(result)

