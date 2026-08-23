class leap_year:
    def __init__(self,year):
        self.year=year
    def check(self):      
        if((self.year%400==0)):
            print("leap year")
        elif(self.year%4 ==0):
            print("leap year")
        else:
            print("Not a leap year")
year=int(input("Enter year:"))
l=leap_year(year)
l.check()


