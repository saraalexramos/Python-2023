# Please write a function named list_sum which takes two lists of integers as arguments. The function returns a new list which contains the sums of the items at each index in the two original lists. You may assume both lists have the same number of items.

def list_sum (list1, list2):
    sum_list = []
    i = 0
    while i < len(list1):
        sum_list.append(list1[i] + list2[i])
        i += 1
    return sum_list