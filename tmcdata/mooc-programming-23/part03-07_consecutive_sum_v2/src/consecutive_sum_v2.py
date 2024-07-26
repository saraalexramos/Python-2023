limit = int(input("Limit: "))
x = 0
sum = 0
strsum = "1 "

while sum < limit:
    x += 1
    sum += x
    if x > 1:
        strsum += f"+ {x} "
print (f"The consecutive sum: {strsum}= {sum}")