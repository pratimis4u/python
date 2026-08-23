def check(): 
    s=input("Enter Character: ")
    if s.isupper(): 
        print("Upercase")
    elif s.islower():
        print("Lowercase")
    elif s.isdigit():
        print("Character is Digit")
    else:
        print("Special")   
check()