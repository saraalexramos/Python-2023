wage = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
day = input("Day of the week: ")

daily_wages = wage * hours

condition = day == "Sunday"
if condition:
    daily_wages *= 2

print(f"Daily wages: {daily_wages} euros")