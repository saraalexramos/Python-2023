''' 
Let's expand the program created in the previous exercise. Now also the exam points awarded to each student are contained in a CSV file.
The contents of the file follow this format:

id;e1;e2;e3
12345678;4;1;4
12345687;3;5;3

In the above example the student whose student number is 12345678 was awarded 4+1+4 points in the exam, which equals a total of 9 points.

The program should again ask the user for the names of the files. Then the program should process the files and print out a grade for each student.

'''

from sys import path

path.append("G:\\PROG\\Python\\tmcdata\\tmcdata\\mooc-programming-23\\part06-04_course_grading_part_2\\src\\students1.csv")
path.append("G:\\PROG\\Python\\tmcdata\\tmcdata\\mooc-programming-23\\part06-04_course_grading_part_2\\src\\exercises1.csv")
path.append("G:\\PROG\\Python\\tmcdata\\tmcdata\\mooc-programming-23\\part06-04_course_grading_part_2\\src\\exam_points1.csv")


student_file = input("Student information: ")
exercises_file = input ("Exercises completed: ")
exam_file = input("Exam points: ")

'''
student_file = "G:\\PROG\\Python\\tmcdata\\tmcdata\\mooc-programming-23\\part06-04_course_grading_part_2\\src\\students1.csv"
exercises_file = "G:\\PROG\\Python\\tmcdata\\tmcdata\\mooc-programming-23\\part06-04_course_grading_part_2\\src\\exercises1.csv"
exam_file = "G:\\PROG\\Python\\tmcdata\\tmcdata\\mooc-programming-23\\part06-04_course_grading_part_2\\src\\exams_points1.csv"
'''

'''
student_file = "students1.csv"
exercises_file = "exercises1.csv"
exam_file = "exams_points1.csv"
'''

names = {}
exercises = {}
exams = {}


with open(student_file) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        names[parts[0]]= [f"{parts[1].strip()}" , f"{parts[2].strip()}"]

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

with open(exam_file) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        sum = 0
        for number in parts:
            if int(number) > 100:
                continue
            sum += int(number)
        exams[parts[0]] = sum


for id in names.keys():
    exercises_points = ((exercises[id] * 100) / 40) // 10
    exam_points = exams[id]
    total_points = exercises_points + exam_points

    if total_points <= 14:
        print(f"{names[id][0]} {names[id][1]} 0")
    elif 15 <= total_points <= 17:
        print(f"{names[id][0]} {names[id][1]} 1")
    elif 18 <= total_points <= 20:
        print(f"{names[id][0]} {names[id][1]} 2")
    elif 21 <= total_points <= 23:
        print(f"{names[id][0]} {names[id][1]} 3")
    elif 24 <= total_points <= 27:
        print(f"{names[id][0]} {names[id][1]} 4")
    elif total_points >= 28:
        print(f"{names[id][0]} {names[id][1]} 5")