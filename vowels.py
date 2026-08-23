def vowel():
    check=("A","E","I","O","U","a","e","i","o","u")
    s=input("Enter string: ")
    c=0
    for i in s:
        for j in check:
            if i==j:
                c=c+1
                print(i)
    print(c)
vowel()
                
    