def password(str):
    u=l=n=s=c=0
    for i in str:
        c=c+1
    for i in str:
        if i.isupper():
            u=u+1
        elif i.islower():
            l=l+1
        elif i.isdigit():
            n=n+1
        else:
            s=s+1
    if c>=8:
        if u>0:
            if l>0:
                if n>0:
                    if s>0:
                        print("strong Password")
                    else:
                        print("Add special character")
                else:
                    print("Add digits")                
            else:
                print("Add lowercase character")
        else:
            print("Add uppercase character")
    else:
        print("Password must be atleast 8 character long")
p=input("Enter Password: ")
password(p)