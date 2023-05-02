# Please write a function named longest(strings: list), which takes a list of strings as its argument. The function finds and returns the longest string in the list. You may assume there is always a single longest string in the list.

def longest(list):
    length = len(list[0])
    long_word = list[0]
    for word in list:
        if len(word) > length:
            long_word = word
            length = len(word)
        else:
            continue
    return long_word
