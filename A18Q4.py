

def CheckReapet(n):

    Rcount = int(input("Enter Element to Search: "))

    Elements = 0

    for i in n:
        if i == Rcount:
            Elements = Elements + 1
            i = i+1
    return Elements


def main():
    N = int(input("Enter Number: "))

    
    Data = []
    for i in range (1,N+1):
        D1 = (int (input("Enter Data: ")))
        Data.append(D1)
    print(Data)

    Ret = CheckReapet(Data)
    print(Ret)

if __name__=="__main__":
    main()