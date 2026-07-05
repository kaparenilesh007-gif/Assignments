Multi = lambda No1,No2: (No1 * No2)

def main():
    No1 = int(input("Enter 1st Number: "))
    No2 = int(input("Enter 2nd Number: "))
    Ret = Multi(No1, No2)
    print("Multiplication is:",Ret)

if __name__=="__main__":
    main()