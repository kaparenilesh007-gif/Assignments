def NaturalSum(no):
    
    Nsum = 0
    for i in range(1,no+1):
        Nsum = Nsum +i
    return(Nsum)

def main():
    No1 = int(input("Enter Number: "))

    Ret = NaturalSum(No1)

    print("Sum of Entered Natural Number is: ",Ret)

if __name__=="__main__":
    main()
