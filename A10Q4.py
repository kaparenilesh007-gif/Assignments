from MarvellousLibrary import CheckEvenN
'''
def CheckEven(Element):
    ChEv = list()
    for no in range(1,Element+1):
        if no%2==0:
            ChEv.append(no)
    return ChEv
'''

def main():
    EvenNumber = int(input("Enter Numebr:"))

    Ret = CheckEvenN(EvenNumber)
    print("Enven Numbe list upto Entered Number: ",Ret)

if __name__=="__main__":
    main()