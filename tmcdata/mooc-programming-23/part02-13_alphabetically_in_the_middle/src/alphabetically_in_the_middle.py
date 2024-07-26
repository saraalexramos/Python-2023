n1 = input("1st letter: ")
n2 = input("2nd letter: ")
n3 = input("3th letter: ")
if n2 < n1 < n3 or n3 < n1 < n2:
    print(f"The letter in the middle is {n1}")
if n1 < n2 < n3 or n3 < n2 < n1:
    print(f"The letter in the middle is {n2}")
if n1 < n3 < n2 or n2 < n3 < n1:
    print(f"The letter in the middle is {n3}")