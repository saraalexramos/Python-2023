# Please write a function named same_chars, which takes one string and two integers as arguments. 
# The integers refer to indexes within the string. The function should return True if the two characters at the indexes specified are the same. 
# Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.

def same_chars(string, num1, num2):
    if num1 >= len(string) or  num2 >= len(string):
        return False
    
    elif string[num1] == string[num2]:
        return True
    else:
        return False
    



# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))