word = input("Please type in a word: ")
letter = input("Please type in a character: ")

while True:
    index = word.find(letter)
    if index == -1:
        break
    elif len(word[index:index+3]) < 3:
        break
    print(word[index:index+3]) 
    word = word[(index+1):] 