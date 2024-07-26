'''
Please define a new class named Clock which expands on the capabilities of your Stopwatch class. It should work as follows:

clock = Clock(23, 59, 55)
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)

clock.set(12, 5)
print(clock)

Sample output

23:59:55
23:59:56
23:59:57
23:59:58
23:59:59
00:00:00
00:00:01
12:05:00
'''


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        if self.seconds == 59:
            if self.minutes == 59:
                if self.hours == 23:
                    self.hours = 0
                    self.minutes = 0
                    self.seconds = 0
                else:
                    self.hours += 1
                    self.minutes = 0
                    self.seconds = 0
            else:
                self.minutes += 1
                self.seconds = 0
        else:
            self.seconds += 1

    def set(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"