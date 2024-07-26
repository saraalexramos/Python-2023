'''
The Python module string contains some string constants, which define certain groups of characters. These include for example lowercase letters and punctuation characters. Please familiarize yourself with these constants, and then write a function named separate_characters(my_string: str). The function takes a string as its argument, and it should separate the characters in the string into three other strings, and return these in a tuple:

    The first string should contain the lowercase and uppercase ASCII letters (string constant ascii_letters)
    The second string should contain all punctuation characters defined by the string constant punctuation
    The third string should contain all the other characters (including whitespace)


'''
import string

def separate_characters(my_string : str):
    letters = ""
    punctuation = ""
    other_chars = ""

    for char in my_string:
        if char in string.ascii_letters:
            letters += char
        elif char in string.punctuation:
            punctuation += char
        else:
            other_chars += char

    return (letters, punctuation, other_chars)


if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])