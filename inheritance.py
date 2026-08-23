class Course:
    def __init__(self,course_id,course_name,year,seats):
        self.course_id=course_id
        self.course_name=course_name
        self.year=year
        self.seats=seats
    def display(self):
        print("Course id: ",self.course_id)
        print("Course Name: ",self.course_name)
        print("YEAR",self.year)
        print("SEATS",self.seats)


class Sports:
    def __init__(self,name):
        self.name=name
    def display1(self):
        print("Sports Name: ",self.name)



class Student(Course,Sports):
    def __init__(self,sid,name,age,dep,mob,email):
        self.sid=sid
        self.name=name
        self.age=age
        self.dep=dep
        self.mob=mob
        self.email=email
    def display(self):
        print("NAME: ",self.name)
        print("AGE: ",self.age)
        print("Department: ",self.dep)
        print("MOBILE: ",self.mob)
        print("EMAIL: ",self.email)
        super().display1()
        super().display()
        


dept=Course(101,"MCA",2,30)
spt=Sports("Badminton")
std=Student("MCA016","Neha Chaurasia",20,101,"8299727188","nehachaurasiya060@gmail.com")
std.display()

