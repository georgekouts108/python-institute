class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        #
        # Write code here
        #
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        

    def __str__(self):
        #
        # Write code here
        #
        hrs = ('0' if self.hours < 10 else '') + str(self.hours)
        mins = ('0' if self.minutes < 10 else '') + str(self.minutes)
        secs = ('0' if self.seconds < 10 else '') + str(self.seconds)
        return hrs + ':' + mins + ':' + secs

    def next_second(self):
        #
        # Write code here
        #
        self.seconds = (self.seconds + 1) % 60
        if self.seconds == 0:
            self.minutes = (self.minutes + 1) % 60
            if self.minutes == 0:
                self.hours = (self.hours + 1) % 24
            
    def prev_second(self):
        #
        # Write code here
        #
        self.seconds = 59 if (self.seconds == 0) else ( (self.seconds - 1) % 60)
        
        if self.seconds == 59:
            self.minutes = ((self.minutes - 1) % 60) if (self.minutes != 0) else 59
            
            if self.minutes == 59:
                self.hours = ((self.hours - 1) % 24) if (self.hours != 0) else 23
 
timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
