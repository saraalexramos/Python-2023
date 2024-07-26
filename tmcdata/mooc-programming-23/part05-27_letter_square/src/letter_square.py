# This final exercise in this part is a relatively demanding problem solving task. It can be solved in many different ways. Even though this current section in the material covers tuples, tuples are not necessarily the best way to go about solving this.

# Please write a program which prints out a square of letters as specified in the examples below. You may assume there will be at most 26 layers.




def letter_square(layers):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    if layers == 1:
        return "A"
    else: # more than 1 layer
        result = []
        result.append((layers*2-1) * letters[layers-1])
        
        x = 0
        i = 0
        while x < layers * 2 - 3:
            result.append(f"{letters[layers-1]}"+f"{(letter_square(layers-1)[i])}"+f"{letters[layers-1]}")
            x += 1
            i += 1

        result.append((layers*2-1) * letters[layers-1])

        return result
    

layers = int(input("Layers: "))
for row in letter_square(layers):
    print(row)