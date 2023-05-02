# In this exercise you will write a program for printing out grade statistics for a university course.
# The program asks the user for results from different students on the course. These include exam points and numbers of exercises completed. The program then prints out statistics based on the results.
# Exam points are integers between 0 and 20. The number of exercises completed is an integer between 0 and 100.
# The program kees asking for input until the user types in an empty line. You may assume all lines contain valid input, which means that there are two integers on each line, or the line is empty.

# When the user types in an empty line, the program prints out statistics. They are formulated as follows:
# The exercises completed are converted into exercise points, so that completing at least 10% of the exercises grants one point, 20% grants two points, and so forth. 
# Completing all 100 exercises grants 10 exercise points. The number of exercise points granted is an integer value, rounded down.
#   0 - 14 points - 0 (fail)
#   15- 17 points - 1
#   18- 20 points - 2
#   21- 23 points - 3
#   24- 27 points - 4
#   28- 30 points - 5
# There is also an exam cutoff threshold. If a student received less than 10 points from the exam, they automatically fail the course, regardless of their total number of points.
# With the example input from above the program would print out the following statistics:
'''
Statistics:
Points average: 14.5
Pass percentage: 75.0
Grade distribution:
  5:
  4:
  3: *
  2:
  1: **
  0: *
'''


ex_completed = []
exam_points = []
total_points = []
grades = []

def inputs():

    global exam_points # to store all the exam points from inputs
    global ex_completed # to store all the exercises completed from inputs

    while True:
        input1 = input("Exam points and exercises completed: ")
        if input1 == "":
            break
        input_split = input1.split() # create a temporary list "input_split" to save the 2 numbers from input1
        
        exam_points.append(int(input_split[0])) # first number goes to "exam_points" list
        ex_completed.append(int(input_split[1])) # second and last number goes to "ex_completed" list
    
    # At this point there are 2 lists with all the input numbers (as integers).
    # exam_points = [15, 10, 11, 4]
    # ex_completed = [87, 55, 40, 17]
    
    return exam_points
    return ex_completed
    '''
    print(exam_points)
    print(ex_completed)
    '''

def points():
    
    #--------------------------- to convert exercises completed to exercises points ------------------
    global ex_completed
    global exam_points
    global grades

    ex_points = []
    
    for i in range (len(ex_completed)):
        points = ex_completed[i] // 10
        ex_points.append(points)
    # ex_points [8, 5, 4, 1]

    #--------------------------- sum ex_points with exam_points to get total_points -------------------
    global total_points

    for i in range (len(ex_points)):
        sum = ex_points[i] + exam_points[i]
        total_points.append(sum)

    for i in range (len(total_points)):
        if exam_points[i] < 10 or total_points[i] <= 14:
            grade = 0
            grades.append(grade)
            continue
        elif 15 <= total_points[i] <= 17:
            grade = 1
            grades.append(grade)
        elif 18 <= total_points[i] <= 20:
            grade = 2
            grades.append(grade)
        elif 21 <= total_points[i] <= 23:
            grade = 3
            grades.append(grade)
        elif 24 <= total_points[i] <= 27:
            grade = 4
            grades.append(grade)
        elif 28 <= total_points[i] <= 30:
            grade = 5
            grades.append(grade)

    


def statistics():
    global total_points
    global grades

    print("Statistics:")

    # average points calculation
    pts_sum = 0

    for num in total_points:
        pts_sum += num
    nums = len(total_points)
    avg_pts = pts_sum / nums

    # pass percentage calculation
    count = 0

    for i in range (len(grades)):
        if grades[i] >= 1:
            count += 1
    
    percen = (count * 100) / (len(total_points))

    print("Points average:", avg_pts)
    print("Pass percentage:", "{:.1f}".format(percen))
    

    # Grade Distribution
    print("Grade distribution:")

    print("5:", end= " ")
    for n in grades:
        if n == 5:
            print("*", end = "")
    print()
    print("4:", end= " ")
    for n in grades:
        if n == 4:
            print("*", end = "")
    print()
    print("3:", end= " ")
    for n in grades:
        if n == 3:
            print("*", end = "")
    print()
    print("2:", end= " ")
    for n in grades:
        if n == 2:
            print("*", end = "")
    print()
    print("1:", end= " ")
    for n in grades:
        if n == 1:
            print("*", end = "")
    print()
    print("0:", end= " ")
    for n in grades:
        if n == 0:
            print("*", end = "")



inputs()
points()
statistics()