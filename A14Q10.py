Largest = lambda No1,No2,No3 : (No1 if No1>No2>No3 else No2 if No2>No3 else No3 )

def main():
    No1 = int(input("Enter 1st Number: "))
    No2 = int(input("Enter 2nd Number: "))
    No3 = int(input("Enter 3rd Number: "))
    Ret = Largest(No1, No2, No3)
    print("Largest Number is:",Ret)

if __name__=="__main__":
    main()