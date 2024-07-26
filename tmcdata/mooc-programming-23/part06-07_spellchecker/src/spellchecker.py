'''
Please write a program which asks the user to type in some text. 
Your program should then perform a spell check, and print out feedback to the user, so that all misspelled words have stars around them. 
Please see the two examples below:

Write text: We use ptython to make a spell checker
We use *ptython* to make a spell checker

Write text: This is acually a good and usefull program
This is *acually* good and *usefull* program

The case of the letters should be irrelevant to the functioning of your program.

The exercise template includes the file wordlist.txt, which contains all the words the spell checker should accept as correct.

'''


text = input("Write text: ")


words = text.split(" ")

correct_words = []
with open("wordlist.txt") as new_file:
    for line in new_file:
        correct_words.append(str(line.strip().lower()))

for index, word in enumerate(words):
    if word.lower() in correct_words:
        continue
    else:
        words[index] = f"*{word}*"

for word in words:
    print(word, end = " ")
