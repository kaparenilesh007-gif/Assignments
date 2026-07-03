
Addition = lambda No1,No2 : No1+No2

Substraction = lambda No1,No2 : No1-No2

Multiplication = lambda No1,No2 : No1*No2

Division = lambda No1,No2 : No1/No2

def main():
    No1 = int(input("Enter No1: "))
    No2 = int(input("Enter No2: "))

    Add = Addition(No1,No2)
    print("Addition is: ",Add)

    Sub = Substraction(No1,No2)
    print("Substraction is: ",Sub)

    Mult = Multiplication(No1,No2)
    print("Multiplication is: ",Mult)

    Div = Division(No1,No2)
    print("Division is: ",Div)

    
if __name__=="__main__":
    main()