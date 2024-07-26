word = input("Word: ")

length = len(word)
start = (28 - length) // 2
str = "*"
strstart= " "*start

print (30 * str)
if length % 2 == 0:
    print ("*"+ strstart + word + strstart + "*")
else: 
    print ("* "+ strstart + word + strstart + "*")
print (30 * str)