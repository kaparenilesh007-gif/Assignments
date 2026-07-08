import threading


def Even(Element):

    ChEv = list()
    for no in Element:
        if no%2==0:
            if len(ChEv)<10:
                ChEv.append(no)
    print(ChEv)



def Odd(Element):
        
        ChOdd = list()
        for no in Element:
            if no%2!=0:
                if len(ChOdd)<10:
                    ChOdd.append(no)
        print(ChOdd)

def main():

    Size = int(input("Enter the Number of elements: "))

    Arr = list()

    print("Enter the elements: ")
    for i in  range(Size):
        no  = int(input())
        Arr.append(no)


    t1= threading.Thread(target=Even(Arr))
    t2 = threading.Thread(target=Odd(Arr))

if __name__=="__main__":
    main()