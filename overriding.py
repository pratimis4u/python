class rect:    
    def a_rect(self,p,q):
        print("Area",p*q)
    def p_rect(self,p,q): 
        print("Perimeter",2*(p+q))
class shapes(rect):   
    def a_sq(self,p): 
        print("Area",p*p)
    def p_sq(self,p): 
        print("Perimeter",4*p)
    def a_rect(self,p,q): 
        return p*q
    
    
r1=shapes()
print("area of rect: ",r1.a_rect(1,1))
r1.p_rect(2,2)
r1.a_sq(3)
r1.p_sq(4)
