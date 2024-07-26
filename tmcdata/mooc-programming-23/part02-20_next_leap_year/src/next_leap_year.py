year1 = int(input("Year: "))
year2 = year1
while True:
    year2 += 1
    if year2 % 4 == 0:
        if year2 % 100 == 0 and year2 % 400 == 0:
            break
        if year2 % 100 != 0:
            break
print(f"The next leap year after {year1} is {year2}")