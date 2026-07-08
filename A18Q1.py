

def AddOfList(List):

    Sum = 0

    for numbers in List:
        Sum = Sum + numbers

    return Sum
    

def main():
    N = int(input("Enter Number: "))

    Data = []
    for i in range (1,N+1):
        D1 = (int (input("Enter Data: ")))
        Data.append(D1)
    print(Data)
    
    Ret = AddOfList(Data)
    print(Ret)

if __name__=="__main__":
    main()
