import sys

def Add():
    No1 = (int(sys.argv[1]))
    No2 = int((sys.argv[2]))
    
    Ans = No1 + No2

    print(f"Addition of {No1} and {No2} is: {Ans}")

Add()