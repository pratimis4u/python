class rect:    
    def area_rect(self,p,q):         
        print("Area",p*q)
    
class sq:    
    def area_sq(self,p):
        print("Area",p*p)
    
class abc(rect,sq):   
    pass
    
r1=abc()
r1.area_rect(2,3)
r1.area_sq(2)
