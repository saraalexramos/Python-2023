def seven_brothers():
    list1 = ["Aapo", "Juhani", "Timo", "Tuomas", "Lauri", "Eero", "Simeoni"]
    list1.sort()

    i = 0
    while i < len(list1):
        print(list1[i])
        i+=1

if __name__ == "__main__":
    seven_brothers()