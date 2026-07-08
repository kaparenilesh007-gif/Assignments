def Factorial(no):
    Fact = 1
    
    for i in range (1,no+1):
        Fact = Fact*i

    return Fact


def main():

    Num = int(input("Enter Number: "))

    Ret = Factorial(Num)

    print(f"Factorial of {Num} is: {Ret}")
if __name__=="__main__":
    main()
