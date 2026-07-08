import threading


def EvenList(Element):

    ChEv = list()
    Sum = 0

    for no in Element:
        if no%2==0:
            ChEv.append(no)
    print(ChEv)

    for i in ChEv:
        Sum = Sum + i
    print("Addition of Even Numbers is: ",Sum)



def OddList(Element):
        
        ChOdd = list()
        Sum = 0

        for no in Element:
            if no%2!=0:
                    ChOdd.append(no)
        print(ChOdd)
    
        for i in ChOdd:
            Sum = Sum + i
        print("Addition of odd Numbers is: ",Sum)

def main():

    Size = int(input("Enter the Number of elements: "))

    Arr = list()

    print("Enter the elements: ")
    for i in  range(Size):
        no  = int(input())
        Arr.append(no)


    t1= threading.Thread(target=EvenList(Arr))
    t2 = threading.Thread(target=OddList(Arr))

    t1.start()
    t2.start()

if __name__=="__main__":
    main()