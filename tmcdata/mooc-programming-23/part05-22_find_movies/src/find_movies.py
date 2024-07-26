


def find_movies( database: list, search_term : str):

    search_database = [] # a new list to store all the movies with search_term

    for movie in database: # for each movie, it will compare the name to the search term. If the name as it : it will append to new list
        if search_term.lower() in movie["name"].lower():
            search_database.append(movie)
    
    return search_database







if __name__ == "__main__":

    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
                {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
                {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)