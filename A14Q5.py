CheckEven = lambda No :(No%2==0)

def main():
    No = int(input("Enter Number: "))
    Ret = CheckEven(No)
    print("Even: ",Ret)

if __name__=="__main__":
    main()