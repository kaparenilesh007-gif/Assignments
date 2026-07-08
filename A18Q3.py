
def main():
    N = int(input("Enter Number: "))

    Data = []
    for i in range (1,N+1):
        D1 = (int (input("Enter Data: ")))
        Data.append(D1)
    print(Data)

    Minimum = min(Data)
    print(Minimum)


if __name__=="__main__":
    main()