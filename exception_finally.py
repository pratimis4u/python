class zero(Exception):
    pass
try:
    i_num=int(input("Enter a number: "))
    if i_num==0:
        raise zero
    else:
        print(i_num)
except zero:
    print("Input value is zero, Try again")
finally:
    print("Use of finally block")
