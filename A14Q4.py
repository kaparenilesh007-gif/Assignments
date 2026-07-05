MinNo = lambda No1,No2: (No1 if No1<No2 else No2)

def main():
    No1 = int(input("Enter 1st Number: "))
    No2 = int(input("Enter 2nd Number: "))
    Ret = MinNo(No1, No2)
    print("Minimum Number is:",Ret)

if __name__=="__main__":
    main()