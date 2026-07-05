CheckNo = lambda No : (No%5==0)

def main():
    No = int(input("Enter Number: "))
    Ret = CheckNo(No)
    print("Entered Number is Divisible by 5: ",Ret)

if __name__=="__main__":
    main()