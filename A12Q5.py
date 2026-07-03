
def MultiNumbersReverse(no):
    List = []
    for i in range(no,0,-1):
        List.append(i)
        
    return List


def main():
    No = int(input("ENter Number: "))

    Ret = MultiNumbersReverse(No)

    print("MultiNumberReverse are: ",Ret)

if __name__=="__main__":
    main()