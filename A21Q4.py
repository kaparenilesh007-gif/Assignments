


import threading

Addition = 0
Mult = 1
def Sum(List):

    global Addition
    for i in List:
        Addition = (Addition +i)
        i = i +1

    return Addition


def Product(List):

    global Mult
    for i in List:
        Mult = Mult*i
        i = i+1

    return Mult


def main():

    Size = int(input("Enter the Number of elements: "))

    Arr = list()

    print("Enter the elements: ")
    for i in  range(Size):
        no  = int(input())
        Arr.append(no)


    t1 = threading.Thread(target=Sum, args=(Arr,))
    t2 = threading.Thread(target=Product, args=(Arr,))

    t1.start()
    t2.start()
 
    t1.join()
    t2.join()
    
    print("Sum of elements is",Addition )
    print("Product of elements is", Mult)

if __name__=="__main__":
    main()