def squared(string, num):
    
    
    y = 0
    x = 0
    count = 0
    while x <= (len(string) - 1):
        print (string[x], end = "")
        count += 1
        if count == num :
            print()
            count = 0
            y += 1
        x += 1 
        if x >= (len(string)):
            x = 0
        if y >= num:
            break
            
if __name__ == "__main__":
    squared("aybabtu", 5)