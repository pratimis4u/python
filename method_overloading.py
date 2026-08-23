class overloading:
    def __init__(self):
        pass
    def add(self,*arg):
        sum=0
        for i in arg:
            sum=sum+i
        print("Sum=",sum)
obj=overloading()
obj.add(10)
obj.add(10,20)
obj.add(10,20,30)
obj.add(10,20,30,40)
    