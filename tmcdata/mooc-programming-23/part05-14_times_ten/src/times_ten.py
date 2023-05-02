# Please write a function named times_ten(start_index: int, end_index: int), which creates and returns a new dictionary. The keys of the dictionary should be the numbers between start_index and end_index inclusive

def times_ten(start_index: int, end_index: int):
    my_dictionary = {} # dictionary to save the keys and values
    i = start_index # a variable to help run all values between start and end index
    
    # cicle to run all the values between start and end index ( with the help of an auxiliar variable "i")
    while i <= end_index: 
        my_dictionary[i] = i * 10 # the key "i" corresponds to the value i * 10
        i += 1
    return my_dictionary
