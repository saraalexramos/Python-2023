# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.seconds == 59:
            if self.minutes == 59:
                self.minutes = 0
                self.seconds = 0
            else:
                self.minutes += 1
                self.seconds = 0
        else:
            self.seconds += 1


    def __str__(self):
        return f"{self.minutes:02d}:{self.seconds:02d}"
        
# Please add to the class definition so that it works as follows:

# watch = Stopwatch()
# for i in range(3600):
#     print(watch)
#     watch.tick()

'''
00:02
.. many more lines printed out
00:59
01:00
01:01
.. many, many more lines printed out
59:58
'''

if __name__ == "__main__":

    watch = Stopwatch()
    for i in range (59*59 + 200):
        print(watch)
        watch.tick()