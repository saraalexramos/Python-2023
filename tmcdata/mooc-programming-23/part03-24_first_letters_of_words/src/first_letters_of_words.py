sent = input("Please type in a sentence: ")
words = sent.split()
i = 0

while i < len(words):
    word = words[i]
    ch = word[0]
    print(ch, end="\n")


    i+=1