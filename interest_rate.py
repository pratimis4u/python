class RBI:
    interest=10
    def __init__(self,interest):
        self.interest=interest
    def rate(self):
        print("Interest rate=",self.interest)
class SBI(RBI):
    def __init__(self):
        pass
    def rate(self):
        print("Interest rate=",10)
s=SBI()
s.rate()