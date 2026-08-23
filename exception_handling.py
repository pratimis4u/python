try:
    x=int(input("Enter a number"))
    y=int(input("Enter a number"))
    z=x/y
    print("z=",z)
except ZeroDivisionError:
    print("You are dividing a number by zero")    