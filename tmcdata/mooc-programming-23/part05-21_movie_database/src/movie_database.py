# Please write a function named add_movie(database: list, name: str, director: str, year: int, runtime: int), which adds a new movie object into a movie database.

# The database is a list, and each movie object in the list is a dictionary. The dictionary should contain the following keys.

# name
# director
# year
# runtime

# The values attached to these keys are given as arguments to the function.


def add_movie(database: list, name: str, director:str, year: int, runtime: int):
    
    dictionary = {} # create a dictionary

    dictionary["name"] = name
    dictionary["director"] = director
    dictionary["year"] = year
    dictionary["runtime"] = runtime

    database.append(dictionary) #append the dictionary to the database list

