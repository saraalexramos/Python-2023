# Please write a function named all_the_longest, which takes a list of strings as its argument. 
# The function should return a new list containing the longest string in the original list. If more than one are equally long, the function should return all of the longest strings.


def all_the_longest(list):
    length = 0
    longest_words= []

    for word in list:
        word_length = len(word)

        if word_length > length:
            length = word_length
        else:
            continue
    
    for word in list:
        if len(word) == length:
            longest_words.append(word)
    
    return longest_words

