CheckOdd = lambda No :(No%2!=0)

def main():
    No = int(input("Enter Number: "))
    Ret = CheckOdd(No)
    print("Odd: ",Ret)

if __name__=="__main__":
    main()