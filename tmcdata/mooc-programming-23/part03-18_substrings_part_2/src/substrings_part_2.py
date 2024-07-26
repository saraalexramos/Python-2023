str = input("Please type in a string: ")
x = len(str)-1

while x >= 0:
    print(str[x:len(str)+1])
    x -= 1