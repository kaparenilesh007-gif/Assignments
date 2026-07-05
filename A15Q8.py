def InputData():
    Data1 = []
    
    print("Enter Five Numbers: ")
    No = int(input())
    Data1.append(No)

    No = int(input())
    Data1.append(No)

    No = int(input())
    Data1.append(No)

    No = int(input())
    Data1.append(No)

    No = int(input())
    Data1.append(No)

    return Data1

Number = lambda No : No % 5 ==0 and No % 3 == 0

def main():
    Data = []
    Data = InputData()

    Dnumber = list(filter(Number,Data))

    print("Number Divisible by 3 and 5 are : ",Dnumber)


if __name__=="__main__":
    main()

