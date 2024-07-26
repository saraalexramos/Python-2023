





def matrix_sum():
    with open("matrix.txt") as new_file:  # open the file
        sum = 0
        for line in new_file:  # to run all the line of the file
            numbers = line.split(",")
            for number in numbers:
                sum += int(number)
    return sum

def matrix_max():
    with open("matrix.txt") as new_file:  # open the file
        values = []
        for line in new_file:  # to run all the line of the file
            numbers = line.split(",")
            for number in numbers:
                values.append(int(number))
    return max(values)

def row_sums():
    sums = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            sum = 0
            numbers = line.split(",")
            for number in numbers:
                sum += int(number)
            sums.append(sum)
    return sums
