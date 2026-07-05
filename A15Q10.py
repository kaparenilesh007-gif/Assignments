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

EvenNumber = lambda No : No%2==0

def main():
    Data = []
    Data = InputData()

    Even = len(list(filter(EvenNumber,Data)))

    print("Even Numbers are: ",Even)


if __name__=="__main__":
    main()

