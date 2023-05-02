# Please write a function named length_of_longest, which takes a list of strings as its argument. The function returns the length of the longest string.

def length_of_longest(list):
    length = 0
    for word in list:
        if len(word) > length:
            length = len(word)
        else:
            continue

    return length