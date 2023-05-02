# Please write an improved version of the phone book application. Each entry should now accommodate multiple phone numbers. The application should work otherwise exactly as above, but this time all numbers attached to a name should be printed.

phone_book = {} # adictionary to keep all the phone numbers

# cicle to run until a condition is met to stop
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))

    if command == 1: # search
        name = input("name: ")
        if name in phone_book.keys(): # if the key exists, it prints the phone number corresponding
            if isinstance(phone_book[name], list):
                for number in phone_book[name]:
                    print(number)
            else:
                print(phone_book[name])
        elif name not in phone_book.keys(): # if the key does not exist in dictionary, it will print "no number"
            print("no number")
    elif command == 2: # add
        name = input("name: ")
        phone_number = input("number: ")
        if name not in phone_book.keys():
            phone_book[name] = phone_number # create the key and value for the inputs of the user
        elif name in phone_book.keys():
            existing_number = phone_book.get(name)
            phone_book[name] = [existing_number, phone_number] # create the key and value for the inputs of the user
        print("ok!")
        
    elif command == 3: # quit
        print("quitting...")
        break