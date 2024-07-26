
def rows_of_stars(numbers:list):
    return [("*" * int(number)) for number in numbers]

if __name__ == "__main__":
    rows = rows_of_stars([1])
    for row in rows:
        print(row)