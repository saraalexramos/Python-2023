# Write your solution here

def longest_series_of_neighbours(list):
    counts= []
    count = 1
    i = 0
    while i < len(list)-1:
        if list[i] + 1 == list[i+1] or list[i] -1 == list[i+1]:
            count += 1
            counts.append(count)
        else:
            counts.append(count)
            count = 1
        i += 1
    return max(counts)

if __name__ == "__main__":
    longest_series_of_neighbours([1, 2])