str = input("Please type in a string: ")

reslen = 20 - len(str)
str2 = "*"
resstr = str2*reslen

print(resstr + str)