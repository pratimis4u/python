age=input("enter age:-")
if age>=65:
    print("old")
elif age>=20 and age<65:
    print("adult")
elif age>=13 and age<20:
    print("teenager")
elif age>=4 and age<13:
    print("kid")
elif age>0 and age<4:
    print("baby")
else :
    print("Invalid age")
