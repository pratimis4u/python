def pallindrom():
    s1=input("Enter a string")
    s2=s1[-1: :-1]
    if s1!=s2:
        print("Not a pallindrom")
    else:
        print("Pallindrom")
pallindrom()
            