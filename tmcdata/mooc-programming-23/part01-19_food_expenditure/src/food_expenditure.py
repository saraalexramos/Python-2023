eattimes = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
money_spend = float(input("How much money do you spend on groceries in a week? "))

total_week = (eattimes * price) + money_spend
daily = total_week/7

print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {total_week} euros")
