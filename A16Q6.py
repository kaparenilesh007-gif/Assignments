import sys

def CheckNum():
    
    Num = (int(sys.argv[1]))

    if Num ==0:
        print("Zero")
    elif Num >0:
        print("Possitive Number")
    else:
        print("Number is Negative")

CheckNum()