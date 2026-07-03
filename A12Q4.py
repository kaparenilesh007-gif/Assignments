#append number in list

def MultiNumbers(no):
    List = []
    for i in range(1,no+1):
        List.append(i)
        i+1
    return List


def main():
    No = int(input("ENter Number: "))

    Ret = MultiNumbers(No)

    print("MultiNumbers are: ",Ret)

if __name__=="__main__":
    main()