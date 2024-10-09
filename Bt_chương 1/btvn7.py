class Date:
    def __init__(self, day=1, month=1, year=1):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"Ngày: {self.day:02d}/{self.month:02d}/{self.year}")

    def next(self):
        days_in_month = [31, 28 if self.year % 4 != 0 or (self.year % 100 == 0 and self.year % 400 != 0) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        self.day += 1
        
        if self.day > days_in_month[self.month - 1]:
            self.day = 1
            self.month += 1
            
            if self.month > 12:
                self.month = 1
                self.year += 1

date = Date(15, 10, 2006)
date.display() 
date.next()     
date.display()  
