class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def rem(self):
        return self.a%self.b
n1=int(input("first number: "))
n2=int(input("second number: "))
cal=calculator(n1,n2)
print("Addition of ",n1,"and",n2,"is: ",cal.add())
print("Subtraction of ",n1,"and",n2,"is: ",cal.sub())
print("Multiplication of ",n1,"and",n2,"is: ",cal.mul())
print("Division of ",n1,"and",n2,"is: ",cal.div())
print("remainder of ",n1,"and",n2,"is: ",cal.rem())