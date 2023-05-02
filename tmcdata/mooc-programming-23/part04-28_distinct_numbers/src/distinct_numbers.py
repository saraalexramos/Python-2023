# Please write a function named distinct_numbers, which takes a list of integers as its argument. The function returns a new list containing the numbers from the original list in order of magnitude, and so that each distinct number is present only once.


def distinct_numbers(list):
    list2 = []
    for number in list:
        if number in list2:
            continue
        else:
            list2.append(number)

    list2.sort()
    return list2

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))