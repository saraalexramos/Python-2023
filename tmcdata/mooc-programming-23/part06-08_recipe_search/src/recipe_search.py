'''
The program should read the recipes from a file submitted by the user.
Each recipe consists of three or more lines. The first line has the name of the recipe, the second line contains an integer number representing the
preparation time in minutes, and the remaining line or lines contain the ingredients used, one on each line.

The recipe ends with an empty line, with the exception of the final recipe in the file which just ends with the end of the file. 
So, there can be more than one recipe in a single file


'''
#------------------------------------------------------------------ SEARCH BY NAME --------------------------------------------------



'''Please write a function named search_by_name(filename: str, word: str), which takes a filename and a search string as its arguments. 
The function should go through the file and select all recipes whose name contains the given search string. 
The names of these recipes are then returned in a list.'''


def search_by_name(filename:str, word:str):

    #------------------- read the file and put all information in a list "lines"
    recipes = {}
    lines = []

    with open(filename) as new_file:
            for line in new_file:
                lines.append(line.strip())

    # ------------------- create a dictionary with recipes
    while len(lines) > 0:
        recipe_name = lines[0]
        prep_time = lines[1]
        ingredients = []

        for line in lines[2:]:
            if line == '':
                break
            ingredients.append(line)

        recipes[recipe_name] = {"prep_time": prep_time, "ingredients": ingredients}
        lines = lines[2 + len(ingredients) + 1:]

    # -------------------- FUNCTION STARTS
    found_recipes = []

    for recipe in recipes.keys():
        if word.lower() in recipe.lower():
            found_recipes.append(recipe)

    return found_recipes


#------------------------------------------------------------------ SEARCH BY TIME --------------------------------------------------
'''
Please write a function named search_by_time(filename: str, prep_time: int), which takes a filename and an integer as its arguments. 
The function should go through the file and select all recipes whose preparation time is at most the number given.

The names of these recipes are again returned in a list, but the preparation time should be appended to each name. Please have a look at the example below.'''


def search_by_time(filename: str, prep_time: int):
    #------------------- read the file and put all information in a list "lines"
    recipes = {}
    lines = []

    with open(filename) as new_file:
            for line in new_file:
                lines.append(line.strip())

    # ------------------- create a dictionary with recipes
    while len(lines) > 0:
        recipe_name = lines[0]
        preparation_time = int(lines[1])
        ingredients = []

        for line in lines[2:]:
            if line == '':
                break
            ingredients.append(line)

        recipes[recipe_name] = {"prep_time": preparation_time, "ingredients": ingredients}
        lines = lines[2 + len(ingredients) + 1:]

    # -------------------- FUNCTION STARTS
    found_recipes = []

    for recipe in recipes.keys():
        if recipes[recipe]["prep_time"] <= int(prep_time):
            found_recipes.append(f'{recipe}, preparation time {recipes[recipe]["prep_time"]} min')
    
    return found_recipes




#------------------------------------------------------------------ SEARCH BY INGREDIENT --------------------------------------------------
'''
Please write a function named search_by_ingredient(filename: str, ingredient: str), which takes a filename and a search string as its arguments. 
The function should go through the file and select all recipes whose ingredients contain the given search string.

The names of these recipes are returned in a list just like in the second part, with the preparation time appended.'''


def search_by_ingredient(filename: str, ingredient: str):
     #------------------- read the file and put all information in a list "lines"
    recipes = {}
    lines = []

    with open(filename) as new_file:
            for line in new_file:
                lines.append(line.strip())

    # ------------------- create a dictionary with recipes
    while len(lines) > 0:
        recipe_name = lines[0]
        preparation_time = int(lines[1])
        ingredients = []

        for line in lines[2:]:
            if line == '':
                break
            ingredients.append(line)

        recipes[recipe_name] = {"prep_time": preparation_time, "ingredients": ingredients}
        lines = lines[2 + len(ingredients) + 1:]

    # -------------------- FUNCTION STARTS
    found_recipes = []

    for recipe in recipes.keys():
        if ingredient in recipes[recipe]["ingredients"]:
            found_recipes.append(f'{recipe}, preparation time {recipes[recipe]["prep_time"]} min')

    return found_recipes



if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")

    for recipe in found_recipes:
        print(recipe)
    print()
    found_recipes2 = search_by_time("recipes1.txt", 20)

    for recipe in found_recipes2:
        print(recipe)
    print()
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)