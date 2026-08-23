class A:
    def fun1(self):
        print("In class A")
        
class B(A):
    def fun1(self):
        super.fun1()
        print("In class B")
        
    def fun3(self):
        print("In class B")
B1=B() 
B1.fun1()     
B1.fun3()        
        
        