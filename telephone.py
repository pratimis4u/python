
class Telephone_bill():
    def __init__(self,calls):
        self.calls = calls
        self.bill = 200
    def calculateBill(self):
        if(self.calls <= 100): 
            print("Bill",self.bill)
        elif(self.calls > 100 and self.calls <=150 ):
            temp = 0.6 * (self.calls - 100)
            self.bill += temp
            print("Bill",self.bill+temp)
        elif(self.calls >=150 and self.calls <= 200):
            self.bill += 30
            temp = 0.5 * (self.calls - 150)
            print("Bill",self.bill+temp)
        else:
            self.bill += 30 + 25
            temp = 0.4 * (self.calls - 200)
            print("Bill",self.bill+temp)
x = Telephone_bill(int(input("ENTER NUMBER OF CALLS")))
x.calculateBill()
