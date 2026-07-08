import sys

def FirstEven():
    Num = 21
    Even = []
    for i in range (2, Num, 2):
        Even.append(i)
        i = i+2

    print(Even)

FirstEven()