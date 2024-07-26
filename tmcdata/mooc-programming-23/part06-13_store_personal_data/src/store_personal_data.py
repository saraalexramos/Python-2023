

def store_personal_data(person: tuple):
    with open("people.csv", "w") as file:
        file.write(f"\n{person[0]};{person[1]};{person[2]}")