'''
Please write a function named smallest_average(person1: dict, person2: dict, person3: dict), which takes three dictionary objects as its arguments.

Each dictionary object contains values mapped to the following keys:

    "name": The name of the contestant
    "result1": the first result of the contestant (an integer between 1 and 10)
    "result2": the second result of the contestant (as above)
    "result3": the third result of the contestant (as above)

The function should calculate the average of the three results for each contestant, and then return the contestant whose average result was the smallest. The return value should be the entire dictionary object containing the contestant's information.

'''

def smallest_average(person1: dict, person2: dict, person3: dict):
    mean_person1 = (person1["result1"]+ person1["result2"] + person1["result3"]) /3
    mean_person2 = (person2["result1"]+ person2["result2"] + person2["result3"]) /3
    mean_person3 = (person3["result1"]+ person3["result2"] + person3["result3"]) /3

    if mean_person1 < mean_person2 and mean_person1 < mean_person3:
        return person1

    elif mean_person2 < mean_person1 and mean_person2 < mean_person3:
        return person2

    elif mean_person3 < mean_person2 and mean_person3 < mean_person1:
        return person3
    

if __name__ == "__main__":
    print(smallest_average({"result1": 9,"result2": 9,"result3": 9}, {"result1": 7,"result2": 7,"result3": 7}, {"result1": 8,"result2": 8,"result3": 8}))