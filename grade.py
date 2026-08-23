m1=int(input("marks 1: "))
m2=int(input("marks 2: "))
m3=int(input("marks 3: "))
m4=int(input("marks 4: "))
m5=int(input("marks 5: "))
per=((m1+m2+m3+m4+m5)/500)*100
if per<=100 and per>=0:
    if per<=100 and per>=85:
        print("Grade= A")
    elif per<=84 and per>=70:
        print("Grade= B")
    elif per<=69 and per>=60:
        print("Grade= C")
    elif per<=59 and per>=40:
        print("Grade= D")
    else:
        print("Grade= F")
else:
    print("Invalid Marks")
    
