import sys


def CheckNum():
    Num = int(sys.argv[1])

    if Num%2 ==0:
        print("Even Mumber")
    else:
        print("Odd Number")

CheckNum()
    