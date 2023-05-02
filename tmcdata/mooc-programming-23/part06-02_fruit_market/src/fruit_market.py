# The file fruits.csv contains names of fruits, and their prices, in the format specified in this example:
# banana;6.50
# apple;4.95
# Please write a function named read_fruits, which reads the file and returns a dictionary based on the contents. In the dictionary, the name of the fruit should be the key, and the value should be its price. Prices should be of type float.

def read_fruits():
    fruits = {}

    with open("fruits.csv") as new_file: # open the file
        for line in new_file: # to run all the line of the file
            parts = line.split(";") # to split the line to parts
            name = parts[0] # the first word is the name
            price = float(parts[1]) # the second the price in float type
            fruits[name] = price # add the key and value to the dictionary
    return fruits # return the dictionary
