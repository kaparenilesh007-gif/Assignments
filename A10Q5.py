def CheckOdd(no):
    CheOdd = list()
    for no in range(1,no+1):
        if no%2!=0:
            CheOdd.append(no)
    return CheOdd


def main():
    No1 = int(input("Enter number: "))

    Ret = CheckOdd(No1)

    print("Odd numebrs are: ",Ret)

if __name__=="__main__":
    main()
