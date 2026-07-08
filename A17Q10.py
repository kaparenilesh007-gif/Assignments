

####  Return Addition of digits 

def main():

    Num =int(input("Enter Number: "))
    Digit_Sum = 0
    while Num > 0:
        Digit = Num % 10
        Digit_Sum = Digit_Sum + Digit
        Num = Num // 10

    print(Digit_Sum)
    
if __name__=="__main__":
    main()