# Please write a function named most_common_character, which takes a string argument. 
# The function returns the character which has the most occurrences within the string. If there are many characters with equally many occurrences, the one which appears first in the string should be returned.


def most_common_character(string):
    most_common = max(set(string), key = string.count)
    return most_common