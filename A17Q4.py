def Factor(num1):

    Add = 0
    for i in range (1,num1):
        if num1 % i == 0:
            Add =Add+i

    return Add

def main():
    Num = int(input("Enter Number: "))
    Add = 0

    Ret = Factor(Num)

    print(f"Addition of Factors of {Num} is: {Ret}")


if __name__=="__main__":
    main()