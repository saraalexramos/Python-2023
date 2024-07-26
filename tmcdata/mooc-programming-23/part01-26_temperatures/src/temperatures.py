tempF = float(input(print("")))
tempC = (5/9)*(tempF-32)

print(f"{tempF} degrees Fahrenheit equals {tempC} degrees Celsius")

condition = tempC < 0
if condition:
    print("Brr! It's cold in here!")