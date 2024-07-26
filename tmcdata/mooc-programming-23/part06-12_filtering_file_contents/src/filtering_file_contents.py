'''
The file solutions.csv contains some solutions to mathematics problems:

Arto;2+5;7
Pekka;3-2;1
Erkki;9+3;11

As you can see above, on each line the format is name_of_student;problem;result. All the operations are either addition or subtraction, and each has exactly two operands.

Please write a function named filter_solutions() which

    Reads the contents of the file solutions.csv
    writes those lines which have a correct result into the file correct.csv
    writes those lines which have an incorrect result into the file incorrect.csv

'''

def filter_solutions():

    # delete all information in this files
    with open("correct.csv", "w") as other_file:
        pass
    with open("incorrect.csv", "w") as other_file:
        pass
    
    # read the information in solutions.csv
    with open("solutions.csv", "r") as file:

        for line in file:
            parts = line.strip().split(";")

            if "-" in parts[1]:
                operand1, operand2 = parts[1].split("-")
                expected_result = int(operand1) - int(operand2)
            elif "+" in parts[1]:
                operand1, operand2 = parts[1].split("+")
                expected_result = int(operand1) + int(operand2)
            else:
                continue
            
            result = int(parts[2])

            if result == expected_result:
                with open("correct.csv", "a") as correct_answers:
                    correct_answers.write(line)
            else:
                with open("incorrect.csv", "a") as incorrect_answers:
                    incorrect_answers.write(line)


if __name__ == "__main__":
    filter_solutions()