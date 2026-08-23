def min(bal):
    minimum_bal=2000
    try:
        if bal<minimum_bal:
            raise ValueError("minimum balance in your account")
        else:
            print("Balance=", bal)
    except ValueError as e:
        print(e)
balance=int(input("Enter balance"))
min(balance)    
