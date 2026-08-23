class rect:    
    def area_rect(self,p,q):        
        print("Area",p*q)
    
class sq(rect):    
    def area_sq(self,p):         
        print("Area",p*p)
    
class new(sq):   
    def display(self):
        print("Multilevel Inheritance")
r1=new()
r1.area_rect(2,3)
r1.area_sq(2)
r1.display()