def save_data(lists: list, file_name = "shoppinglist.csv"):
    with open(file_name, "w") as my_file:
        for line in lists:
            my_file.write(line.replace("name: ", "").replace("unit price: ", "").replace("quantity: ", "").replace("total price: ", ""). replace(", ", ";")+"\n")


def load_data(file_name = "shoppinglist.csv"):
    data =[]
    with open(file_name, "r") as my_file:
        for line in my_file:
            parts = line.strip().split(";")
            line_str = f"name: {parts[0]}, unit price: {parts[1]}, quantity: {parts[2]}, total price: {parts[3]}"
            data.append(line_str)
    return data


string_list  = [
    "name: apple, unit price: 1.60€/kg, quantity: 2.2kg, total price: 3.52€",
    "name: potato, unit price: 1.30€/kg, quantity: 5.0kg, total price: 6.50€",
    "name: banana, unit price: 0.95€/kg, quantity: 1.2kg, total price: 1.14€",
    "name: milk, unit price: 1.25€/l, quantity: 2.0l, total price: 2.50€",
    "name: rye bread, unit price: 2.50€/piece, quantity: 3.0pieces, total price: 7.50€"
]

save_data(string_list)
string_list2 = load_data()
print("data", string_list2)
for i in range(len(string_list)):
    print(string_list[i] == string_list2[i])