# Please write a function named older_people(people: list, year: int), which selects all those people on the list who were born before the year given as an argument. 
# The function should return the names of these people in a new list.

def older_people(people: list, year: int):
    older_people = [] # a list to store all the older people
    
    # for each person: if the person were born before year, it will append their name into the list older_people
    for person in people:
        if person[1] < year:
            older_people.append(person[0])

    return older_people