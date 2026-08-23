class car:
    def __init__ (self,n1,price):
        self.n1=n1
        self.price=price
    def display(self):
        print(self.name)
        print(self.n1)
        print(self.price)
        
c1=car("toyota",4800000)
c2=car("fortuner",4500000)
c1.display()
c1.name="maruti"
c1.display()
c2.display()        
        