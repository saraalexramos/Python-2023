x = input("Password: ")

while True:
    pass2 = input("Repeat password: ")
    if x != pass2:
        print("They do not match!")
    if x == pass2:
        break

print("User account created!")