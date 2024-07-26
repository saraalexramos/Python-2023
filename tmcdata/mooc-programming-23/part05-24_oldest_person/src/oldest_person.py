# Please write a function named oldest_person(people: list), which takes a list of tuples as its argument. 
# In each tuple, the first element is the name of a person, and the second element is their year of birth. 
# The function should find the oldest person on the list and return their name.

# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# people = [p1, p2, p3]

# print(oldest_person(people))

# output : Mary

def oldest_person(people: list):
    oldest_age = 0
    oldest_name = ""

    # for each person: if the person is oldest it will save the age and name in helper variables
    for person in people:
        if 2023 - person[1] > oldest_age:
            oldest_age = 2023 - person[1]
            oldest_name = person[0]
    
    return oldest_name
        