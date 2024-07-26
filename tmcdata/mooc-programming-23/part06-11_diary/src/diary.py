# Please write a program which works as a simply diary. The diary entries should be saved in the file diary.txt. 
# When the program is executed, it should first read any entries already in the file.

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    option = int(input("Function: "))

    match option:
        case 0:
            print("Bye now!")
            break

        case 1:
            entry = input("Diary entry: ")

            with open("diary.txt", "a") as diary:
                diary.write(f"{entry}\n")

            print("Diary Saved")

        case 2:
            print("Entries:")
            with open("diary.txt") as diary:
                for line in diary:
                    print(line)

                