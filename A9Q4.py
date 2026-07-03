def Cube(no):
    return no*no*no


def main():
    No = int(input("ENter Number: "))

    Ret = Cube(No)
    print("Cube of entered number is : ",Ret)

if __name__=="__main__":
    main()