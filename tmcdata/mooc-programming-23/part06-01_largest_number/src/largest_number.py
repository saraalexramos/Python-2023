# The file numbers.txt contains integer numbers
# Please write a function named largest, which reads the file and returns the largest number in the file.

def largest():
    numbers = []

    with open("numbers.txt") as new_file:
        for line in new_file:
            numbers.append(int(line))
    return max(numbers)

