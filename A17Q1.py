from Arithmetic import Add,Sub,Mult,Div

def main():
    No1 = int(input("Enter fisrt Number: "))
    No2 = int(input("Enter second Number: "))

    Ans1 = Mult(No1, No2)
    print(f"Multiplication of {No1} and {No2} is: ",Ans1)

    Ans2 = Div(No1, No2)
    print(f"Division of {No1} and {No2} is: ",Ans2)
    
    Ans3 = Add(No1, No2)
    print(f"Addition of {No1} and {No2} is: ",Ans3)

    Ans4 = Sub(No1, No2)
    print(f"Substraction of {No1} and {No2} is: ",Ans4)

if __name__=="__main__":
    main()
