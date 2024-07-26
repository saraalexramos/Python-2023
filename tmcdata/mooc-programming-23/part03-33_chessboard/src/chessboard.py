def chessboard(num):
   
    i = 1
    while i <= num: 
        x = 1 
        if i == 1 or i % 2 != 0:
            while x <= num:
                if x == 1 or x % 2 != 0:
                    print ("1", end = "")
                else:
                    print ("0", end = "")
                x += 1
            i += 1
            print()
        else:
            while x <= num:
                if x == 1 or x % 2 != 0:
                    print ("0", end = "")
                else:
                    print ("1", end = "")
                x += 1
            i += 1
            print()

if __name__ == "__main__":
    chessboard(6)

    