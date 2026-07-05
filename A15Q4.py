from functools import reduce
def InputData():
    Idata =[]

    print("Enter five numbers: ")
    Num = int(input())
    Idata.append(Num)

    Num = int(input())
    Idata.append(Num)


    Num = int(input())
    Idata.append(Num)


    Num = int(input())
    Idata.append(Num)

    Num = int(input())
    Idata.append(Num)

    return Idata


Sum = lambda No1,No2 : No1+No2


def main():
    Data = []

    Data = InputData()

    print("Entered data is: ",Data)

    Fdata = reduce(Sum,Data)
    print("Sum of entered number is : ",Fdata)


if __name__=="__main__":
    main()
