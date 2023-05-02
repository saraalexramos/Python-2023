# Please write a function named anagrams, which takes two strings as arguments. The function returns True if the strings are anagrams of each other. Two words are anagrams if they contain exactly the same characters.


def anagrams(word1, word2):
    list1 = list(word1)
    list2 = list(word2)
    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    return False