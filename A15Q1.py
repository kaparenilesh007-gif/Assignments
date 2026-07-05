def InputData():
    Data = []
    print("Enter five Numbers:")
    Num = int(input())
    Data.append(Num)
    
    Num = int(input())
    Data.append(Num)

    Num = int(input())
    Data.append(Num)

    Num = int(input())
    Data.append(Num)

    Num = int(input())
    Data.append(Num)
    return Data
    
    
Sqaure = lambda no : no*no

def MapX(Task,Element):
    Result =[]
    for no in Element:
        Ret = Task(no)
        Result.append(Ret)
    return Result

def main():
    Data1 = []
    Data1 = InputData()

    print("Entered Data is: ",Data1)

    Mdata = list(MapX(Sqaure,Data1))
    print("Sqaure of each value is ",Mdata)



if __name__=="__main__":
    main()
