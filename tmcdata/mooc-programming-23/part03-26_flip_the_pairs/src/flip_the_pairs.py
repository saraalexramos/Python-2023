num = int(input("Please type in a number: "))
i=1
j=0
x = []

while i <= num: #create a list of numbers from 1 to num
    x.append(i) 
    i+=1

while j < (num-1):
    if x[j] % 2 != 0:
        print(x[j+1])
        print(x[j])
    j+=1
if num % 2 != 0:
    print(x[-1])
    