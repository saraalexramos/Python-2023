# Please write a function named shortest, which takes a list of strings as its argument. The function returns whichever of the strings is the shortest. 
# If more than one are equally short, the function can return any of the shortest strings (there will be no such situation in the tests). You may assume there will be no empty strings in the list.~


def shortest(list):
    length = len(list[0])
    short_word = list[0]
    for word in list:
        if len(word) < length:
            short_word = word
            length = len(word)
        else:
            continue
    return short_word

