
#######################################################         Create a simple student database         #######################################################

# Part 1: adding students
# First write a function named add_student, which adds a new student to the database. Also write a preliminary version of the function print_student, which prints out the information of a single student.

# Part 2: adding completed courses
# Please write a function named add_course, which adds a completed course to the information of a specific student in the database. The course data is a tuple consisting of the name of the course and the grade:

# Part3: repeating courses
# Courses with grade 0 should be ignored when adding course information. Additionally, if the course is already in the database in that specific student's information, the grade recorded in the database should never be lowered if the course is repeated.

# Part 4: summary of database
# Please write a function named summary, which prints out a summary based on all the information stored in the database.



# ----------------------------------------------- function to add a student ------------------------------------------

def add_student(database: dict, name: str):
    database[name] = [] # an empty list to store all the courses and grades information per student


# ---------------------------------------------- function to print a student ----------------------------------------

def print_student(database: dict, name: str):
    
    # if the name already are in database:

    if name in database:
        print(f"{name}:")

        # if the student has no completed courses:
        if database[name] == []:
            print(" no completed courses")

        # if student already has completed courses:
        else:
            print(f" {len(database[name])} completed courses:")
            
            sum_grades = 0 # a helper variable to store the sum of the grades
            
            # to run all the courses, print them and calculate the sum of grades
            for course in database[name]:
                print(f"  {course[0]} {course[1]}")
                sum_grades += course[1]
            print(f" average grade {sum_grades / len(database[name])}")

    
    # the name not in database:
    else: 
        print(f"{name}: no such person in the database")


# ------------------------------------------ function to add completed courses ---------------------------------------

def add_course(database: dict, name: str, course: tuple):
    courses_names = []
    for database_course in database[name]:
        courses_names.append(database_course[0])

    if course[1] > 0:
        if database[name] == []:
            database[name].append(course)

        else:    
            if course[0] in courses_names:
                for course_record in database[name]:
                    if course_record[1] < course[1]:
                        database[name].remove(course_record)
                        database[name].append(course)
            else:
                database[name].append(course)
                
def summary(database:dict):
    print("students", len(database))
    names = []
    completed_courses = []
    average_grades = []

    for student in database:
        names.append(student)
        completed_courses.append(len(database[student]))
    
    for student in database:
        sum = 0
        count = len(database[student])
        for course in database[student]:
            sum += course[1]
        average = sum /count
        average_grades.append(average)

    max_completed_courses = max(completed_courses)
    index = completed_courses.index(max_completed_courses)
    print("most courses completed", max_completed_courses, names[index])
    max_average_grades = max(average_grades)
    index = average_grades.index(max_average_grades)
    print("best average grade", max_average_grades, names[index])
