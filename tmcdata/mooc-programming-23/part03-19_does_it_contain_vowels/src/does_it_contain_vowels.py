str = input("Please type in a string: ")

for i in ["a", "e", "o"]:
    if i in str:
        print (f"{i} found")
    else:
        print (f"{i} not found")
