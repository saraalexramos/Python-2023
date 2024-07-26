str = input("Please type in a word: ")
letter = input("Please type in a character: ")
index = str.find(letter)

result = str[index:index+3]

if index <= len(str)-2 and len(result) >= 3:
    print(result)
    