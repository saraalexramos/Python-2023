
import copy

def invert(dictionary: dict):
    dict_values = []
    dict_keys = []

    # to put all the values in the list:
    for value in dictionary.values():
        dict_values.append(value)
    # to put all the keys in the list
    for key in dictionary.keys():
        dict_keys.append(key)

    dictionary.clear()
    
    i = 0
    while i < len(dict_values):
        dictionary[dict_values[i]] = dict_keys[i]
        i += 1
    
    
