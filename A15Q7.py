def InputData():
    Data1 = []
    
    print("Enter Five Names: ")
    Name = (input())
    Data1.append(Name)

    Name = (input())
    Data1.append(Name)

    Name = (input())
    Data1.append(Name)

    Name = (input())
    Data1.append(Name)

    Name = (input())
    Data1.append(Name)

    return Data1

Length1 = lambda name : len(name)>=5

def main():
    Data = []
    Data = InputData()

    Length = list(filter(Length1,Data))

    print("having length greater than 5: ",Length)


if __name__=="__main__":
    main()

