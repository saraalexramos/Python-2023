''' This program works with two CSV files. One of them contains information about some students on a course:
id;first;last
12345678;peter;pythons
12345687;jean;javanese

The other contains the number of exercises each student has completed each week:

id;e1;e2;e3;e4;e5;e6;e7
12345678;4;1;1;4;5;2;4
12345687;3;5;3;1;5;4;6


'''
from sys import path

path.append("G:\\PROG\\Python\\tmcdata\\tmcdata\\mooc-programming-23\\part06-04_course_grading_part_1\\src\\students1.csv")
path.append("G:\\PROG\\Python\\tmcdata\\tmcdata\\mooc-programming-23\\part06-04_course_grading_part_1\\src\\exercises1.csv")

student_file = input("Student information: ")
exercises_file = input ("Exercises completed: ")

#student_file = "G:\\PROG\\Python\\tmcdata\\tmcdata\\mooc-programming-23\\part06-04_course_grading_part_1\\src\\students1.csv"
#exercises_file = "G:\\PROG\\Python\\tmcdata\\tmcdata\\mooc-programming-23\\part06-04_course_grading_part_1\\src\\exercises1.csv"

#student_file = "students1.csv"
#exercises_file = "exercises1.csv"


names = {}
exercises = {}

with open(student_file) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        names[parts[0]]= [parts[1] , parts[2]]

with open(exercises_file) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        sum = 0
        for number in parts:
            if int(number) > 100:
                continue
            sum += int(number)
        exercises[parts[0]] = sum

for id_names in names.keys():
    for id_exercises in exercises.keys():
        if id_names == id_exercises:
            print(f"{names[id_names][0].strip()} {names[id_names][1].strip()} {exercises[id_exercises]}")