import string
from random import choice



def generate_strong_password(number: int, count_num: bool, count_spe: bool):
    specials= ["!","?","=","+","-","(",")","#"]
    
    choices = ["letter"]
    if count_num == True:
        choices.append("number")
        min_num = 1
    else:
        min_num = 0

    if count_spe == True:
        choices.append("special")
        min_spe = 1
    else:
        min_spe = 0

    password = ""

    while True:
        if len(password) == number:
            break
        x = choice(choices)
        match x:
            case "number":
                password += str(choice(string.digits))
            case "special":
                password += str(choice(specials))
            case "letter":
                password += str(choice(string.ascii_lowercase))
    

    nums = 0
    spes = 0
    letters = 0
    for char in password:
        if char in string.digits:
            nums += 1
        elif char in specials:
            spes += 1
        elif char in string.ascii_lowercase:
            letters += 1

    if nums >= min_num and spes >= min_spe and letters >= 1:
        return password

    else:
        generate_strong_password(number, count_num, count_spe)

