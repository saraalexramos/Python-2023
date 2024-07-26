'''Please write a program which asks for the name of the user and then creates an "inscription" in a file specified by the user. Please see the example below.

Sample output:
Whom should I sign this to: Ada
Where shall I save it: inscribed.txt

The contents of the file inscribed.txt would be

Sample data:
Hi Ada, we hope you enjoy learning Python with us! Best, Mooc.fi Team'''


name = input("Whom should I sign this to: ")
file_name = input("Where shall I save it: ")

with open(file_name, "w") as new_file:
    new_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")
