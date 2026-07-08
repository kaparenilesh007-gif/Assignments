import sys


def Reverse():
    No = (int(sys.argv[1]))
    
    Num=[]
    
    for i in range(No,0,-1):
        Num.append(i)
    print(Num)

Reverse()