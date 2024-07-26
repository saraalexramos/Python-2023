
import random
import string

def generate_password(number: int):
    password = ""
    for i in range (number):
        x = random.choice(string.ascii_lowercase)
        password += x

    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))

