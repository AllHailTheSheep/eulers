# how many sundays fell on the first of the month during the 20th century, given only that
# 1/1/1900 was a Monday
class Date:
    def __init__(self, day, month, year, dayname):
        self.days_loop = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        self.day = day
        self.month = month
        self.year = year
        self.days_since_start = 0
        self.start_day = self.days_loop.index(dayname)
    
    def __str__(self):
        return 'MM/DD/YYYY: {self.month}/{self.day}/{self.year}, {dayname}'.format(self=self, dayname=self.getDayName())
    
    def getDayName(self):
        return self.days_loop[(self.start_day + self.days_since_start) % 7]

    def getDay(self):
        return self.day
    
    def getMonth(self):
        return self.month
    
    def getYear(self):
        return self.year
    
    def monthLength(self):
        match self.month:
            case 1:
                return 31
            case 2:
                if self.year % 4 == 0 and self.year % 1000 != 0:
                    return 29
                elif self.year % 1000 == 0 and self.year % 400 == 0:
                    return 29
                else:
                    return 28
            case 3:
                return 31
            case 4:
                return 30
            case 5:
                return 31
            case 6:
                return 30
            case 7:
                return 31
            case 8:
                return 31
            case 9:
                return 30
            case 10:
                return 31
            case 11:
                return 30
            case 12:
                return 31
        
    def addDay(self):
        if self.day + 1 <= self.monthLength():
            self.day += 1
            self.days_since_start += 1
        elif self.day == self.monthLength() and self.month != 12:
            self.day = 1
            self.month += 1
            self.days_since_start += 1
        else:
            self.day = 1
            self.month = 1
            self.year += 1
            self.days_since_start += 1


d = Date(1, 1, 1900, "Monday")
sundays_on_first_of_month = 0
while d.getYear() < 2001:
    if d.getDay() == 1 and d.getDayName() == "Sunday" and d.getYear() > 1900:
        sundays_on_first_of_month += 1
    d.addDay()
print(sundays_on_first_of_month)
