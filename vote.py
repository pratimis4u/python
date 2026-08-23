age=int(input("Enter age: "))
if age>16:
    c=input("Enter country: ")
    c=c.lower()
    if age>=18 and c=="india":
        print("You can vote in",c)
    elif age>=16 and c!="india":
        print("You can vote in",c)
    else:
         print("You can not vote")
         
else:
    print("you can not vote")
        