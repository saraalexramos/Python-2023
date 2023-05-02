# Please write a function named histogram, which takes a string as its argument. 
# The function should print out a histogram representing the number of times each letter occurs in the string. Each occurrence of a letter should be represented by a star on the specific line for that letter.


def histogram(string: str):

    letters = [] # a list to save the letters already counted
    # cicle to run all the letters in the string
    for letter in string: 
        # if the letter is not inthe list, it will print the letter followed by the number of times that the letter appeared in string
        if letter not in letters:
            print(letter, "*" * string.count(letter))
            letters.append(letter) # append the letter to the list
        # if the letter is already in tehe list, that means that the letter already was counted, so the program will simply continue to the next letter in string
        elif letter in letters:
            continue

if __name__ == "__main__":
    histogram("statistically")
