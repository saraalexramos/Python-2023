# Please write a function named no_vowels, which takes a string argument. The function returns a new string, which should be the same as the original but with all vowels removed.

# You can assume the string will contain only characters from the lowercase English alphabet a...z.


def no_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    i = 0
    
    while i < len(vowels):
        string= string.replace(vowels[i],"")
        i += 1
    return string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
