
def CheckPrimeN(num):

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

        return True

def AddPrime(num):
     
    Sum = 0
     
    for data in num:
          Sum = Sum + data

    return Sum
     

def main():
    
    NUM = int(input("Enter Number: "))

    Data = []
    for i in range (1,NUM+1):
        D1 = (int (input("Enter Data: ")))
        Data.append(D1)
    print(Data)
    
    Prime_List = []

    for num in Data:
        if CheckPrimeN(num):
            Prime_List.append(num)

    print("Prime Numbers:", Prime_List)

    Ret = AddPrime(Prime_List)

    print(Ret)


if __name__=="__main__":
    main()