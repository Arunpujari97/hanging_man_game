# Banking system 
def baleance(balence):
    print(f"the balence of your account is {balence}")
def deposit(balence):
    ammount=float(input("enter the ammount"))
    if ammount>0:
        balence += ammount
    else:
        print("invalid input")
    return balence
def withdraw(balence):
    ammount=float(input("eneter the ammount"))
    if ammount>balence:
        print("insufficient fund")
    elif ammount< 0:
        print("the enetered ammount is not valid")
    else:
        balence-=ammount
    return balence

def main():
    during=True
    balence=0
    print("1.check balece")
    print("2.deposite the ammount")
    print("3.withdraw the amount")
    print("4.exit")
    while during:
        choice=int(input("enther the  choice "))
        if choice==1:
            baleance(balence)
        elif choice==2:
            balence=deposit(balence)
        elif choice==3:
            balence=withdraw(balence)
        elif choice==4:
            print("exiting .. thankyou")
            break
        else:
            print("invalid choice")

main()
        
