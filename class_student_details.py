class student:
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks
    def display_std(self):
        print(self.id)
        print(self.name)
        print(self.marks)
        
std1=student(1,"supratim",85)
std1.display_std()
std2=student(2,"neha",95)
std2.display_std()