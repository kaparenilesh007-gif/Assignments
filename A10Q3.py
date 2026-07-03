def Factorial(no):
    
    Fact = 1
    for i in range(1, no+1):
        Fact = Fact*i
     
    return(Fact)


def main():
    No1 = int(input("Enter Number: "))
    Ret = Factorial(No1)
    print("Factirial of Entered number is: ",Ret)

if __name__=="__main__":
    main()

'''

'''