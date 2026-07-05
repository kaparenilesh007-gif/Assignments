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


Product = lambda No1,No2 : No1*No2


def main():
    Data = []

    Data = InputData()

    print("Entered data is: ",Data)

    Fdata = reduce(Product,Data)
    print("Product of numbers is : ",Fdata)


if __name__=="__main__":
    main()

