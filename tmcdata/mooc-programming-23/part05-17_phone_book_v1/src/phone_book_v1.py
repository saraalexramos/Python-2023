'''Please write a phone book application. It should work as follows:
command (1 search, 2 add, 3 quit): 2
name: peter
number: 040-5466745
ok!
command (1 search, 2 add, 3 quit): 2
name: emily
number: 045-1212344
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
040-5466745
command (1 search, 2 add, 3 quit): 1
name: mary
no number
command (1 search, 2 add, 3 quit): 2
name: peter
number: 09-22223333
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
09-22223333
command (1 search, 2 add, 3 quit): 3
quitting...
'''


phone_book = {} # adictionary to keep all the phone numbers

# cicle to run until a condition is met to stop
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))

    if command == 1: # search
        name = input("name: ")
        if name in phone_book.keys(): # if the key exists, it prints the phone number corresponding
            print(phone_book[name])
        elif name not in phone_book.keys(): # if the key does not exist in dictionary, it will print "no number"
            print("no number")
    elif command == 2: # add
        name = input("name: ")
        phone_number = input("number: ")
        print("ok!")
        phone_book[name] = phone_number # create the key and value for the inputs of the user
    elif command == 3: # quit
        print("quitting...")
        break