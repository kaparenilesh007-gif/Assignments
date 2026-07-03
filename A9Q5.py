def CheckDiv(no):
    if no%3 ==0 and no%5==0:
        print("Number is Divisible by 3 and 5")
    else:
        print("Number is NOT Divisible by 3 and 5")


def main():
    No = int(input("Enter Number: "))

    CheckDiv(No)


if __name__=="__main__":
    main()
