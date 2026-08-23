class rect:    
    def area_rect(self,p,q): 
        """This method takes input of length and breadth of rectangle and prints area"""
        print("Area of rectangle: ",p*q)
    def perimeter_rect(self,p,q): 
        """This method takes input of length and breadth of rectangle and prints perimeter"""
        print("Perimeter of rectangle: ",2*(p+q))
class shapes(rect):   
    pass
    
r1=shapes()
r1.area_rect(2,3)
r1.perimeter_rect(3,4)
