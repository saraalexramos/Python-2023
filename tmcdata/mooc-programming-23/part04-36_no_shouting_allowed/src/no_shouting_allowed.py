# Please use the isupper method to write a function named no_shouting, which takes a list of strings as an argument. 
# The function returns a new list, containing only those items from the original which do not consist of solely uppercase characters.

def no_shouting(list):
    new_list = []
    for word in list:
        if word.isupper():
            continue
        else:
            new_list.append(word)
    return new_list