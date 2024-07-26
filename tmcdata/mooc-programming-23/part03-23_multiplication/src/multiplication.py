num = int(input("Please type in a number: "))
x=1

while x <= num:
    i = 1
    while i <= num:
        result= x *i
        print(f"{x} x {i} = {result}" )
        i += 1
    x +=1