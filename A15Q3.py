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


Odd = lambda No1: No1%2==1


def main():
    Data = []

    Data = InputData()

    print("Entered data is: ",Data)

    Fdata = list(filter(Odd,Data))
    print("Odd Numbers are: ",Fdata)


if __name__=="__main__":
    main()
