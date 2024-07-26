text = ""
attempts = 0

while True:
    word = input("Please type in a word: ")
    attempts += 1
    if attempts > 1:
        if word == text.split().pop(-1):
            break
    if word == "end":
        break
    text = text + word + " "
    
print(text)