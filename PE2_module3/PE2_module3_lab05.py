class WeekDayError(Exception):
    pass
	

class Weeker:
    #
    # Write code here.
    #
    DAYS = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

    def __init__(self, day):
        #
        # Write code here.
        #
        if day.lower() not in Weeker.DAYS:
            raise WeekDayError()
        self.day = day.title()

    def __str__(self):
        #
        # Write code here.
        #
        return self.day

    def add_days(self, n):
        #
        # Write code here.
        #
        i = Weeker.DAYS.index(self.day.lower())
        self.day = Weeker.DAYS[(i + n) % 7].title()
        

    def subtract_days(self, n):
        #
        # Write code here.
        #
        i = Weeker.DAYS.index(self.day.lower())
        count = n
        j = i
        while count > 0:
            if j > 0:
                j -= 1
            else:
                j = 6
            count -= 1
        self.day = Weeker.DAYS[j].title()

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
