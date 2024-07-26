students_course = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))
if (students_course % group_size == 0):
    number_groups = students_course // group_size
else:
    number_groups = (students_course // group_size) + 1
print(f"Number of groups formed: {number_groups}")
