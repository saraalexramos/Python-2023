# Please write a function named count_matching_elements(my_matrix: list, element: int), which takes a two-dimensional array of integers and a single integer value as its arguments.
# The function then counts how many elements within the matrix match the argument value.


def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for row in my_matrix:
        for number in row:
            if number == element:
                count += 1
    return count

