# Please write a program which asks the user which editor they are using. The program should keep on asking until the user types in Visual Studio Code.

while True:
    editor = input("Editor: ")
    if editor.lower() == "visual studio code":
        print("an excellent choice!")
        break
    if editor.lower() == "word" or editor.lower() == "notepad":
        print("awful")
        continue
    print("not good")


