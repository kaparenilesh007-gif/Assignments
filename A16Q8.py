'''
def StarPrint(No):

    SP = []
    while No>=0:
        SP.append("*")
        No = No-1
    return SP

def main():

    Num = (int(input("Enter Number: ")))

    Ret = StarPrint(Num)

    print(Ret)
    

if __name__=="__main__":
    main()

'''
import sys

def StarPrint():
    Num = (int(sys.argv[1]))
    print(" * "*Num)

    # Star =[]
    # while Num >=0:
    #     Star.append("*")
    #     Num = Num-1
    #print(Star)

StarPrint()