'''
This exercise will continue from the previous one. Now we shall print out some statistics based on the CSV files.
Each row contains the information for a single student. 
The number of exercises completed, the number of exercise points awarded, the number of exam points awarded, the total number of points awarded, and the grade are all displayed in tidy columns. 
The width of the column for the name should be 30 characters, while the other columns should be 10 characters wide.


Student information: students1.csv
Exercises completed: exercises1.csv
Exam points: exam_points1.csv

name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
pekka peloton                 21        5         9         14        0
jaana javanainen              27        6         11        17        1
liisa virtanen                35        8         14        22        3



'''



from sys import path

path.append("G:\\PROG\\Python\\tmcdata\\tmcdata\\mooc-programming-23\\part06-04_course_grading_part_3\\src\\students1.csv")
path.append("G:\\PROG\\Python\\tmcdata\\tmcdata\\mooc-programming-23\\part06-04_course_grading_part_3\\src\\exercises1.csv")
path.append("G:\\PROG\\Python\\tmcdata\\tmcdata\\mooc-programming-23\\part06-04_course_grading_part_3\\src\\exam_points1.csv")


student_file = input("Student information: ")
exercises_file = input ("Exercises completed: ")
exam_file = input("Exam points: ")

'''
student_file = "G:\\PROG\\Python\\tmcdata\\tmcdata\\mooc-programming-23\\part06-04_course_grading_part_3\\src\\students1.csv"
exercises_file = "G:\\PROG\\Python\\tmcdata\\tmcdata\\mooc-programming-23\\part06-04_course_grading_part_3\\src\\exercises1.csv"
exam_file = "G:\\PROG\\Python\\tmcdata\\tmcdata\\mooc-programming-23\\part06-04_course_grading_part_3\\src\\exams_points1.csv"

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

name = "name"
exec_nbr = "exec_nbr"
exec_pts = "exec_pts."
exm_pts = "exm_pts."
tot_pts = "tot_pts."
grade = "grade"
print(f"{name:30} {exec_nbr:10} {exec_pts:10} {exm_pts:10} {tot_pts:10} {grade:10}")

for id in names.keys():
    exercises_points = ((exercises[id] * 100) / 40) // 10
    exam_points = exams[id]
    total_points = exercises_points + exam_points

    if total_points <= 14:
        grade = 0
    elif 15 <= total_points <= 17:
        grade = 1
    elif 18 <= total_points <= 20:
        grade = 2
    elif 21 <= total_points <= 23:
        grade = 3
    elif 24 <= total_points <= 27:
        grade = 4
    elif total_points >= 28:
        grade = 5
    
    print(f"{names[id]:30} {exercises[id]:<10} {exercises_points:<10} {exam_points:<10} {total_points:<10} {grade:<10}")