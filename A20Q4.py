
import threading

def Small(Data):

    print("Thread ID of Small Thread is: ",threading.get_ident())
    print("Thread Name is 'Small' ")

    a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    Sum = 0

    for i in Data:
        if i in a:
            Sum = Sum + 1
            # i = i+1
    print(Sum)


def Capital(Data):
    
    print("Thread ID of Capital Thread is: ",threading.get_ident())
    print("Thread Name is 'Capital' ")

    A = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
    Sum = 0

    for i in Data:
        if i in A:
            Sum = Sum + 1
            #i = i+ 1
    print(Sum)


def Digits(Data):
    
    print("Thread ID of DIgits Thread is: ",threading.get_ident())
    print("Thread Name is 'Digits' ")

    Num = ["0","1","2","3","4","5","6","7","8","9"]
    
    Sum = 0

    for i in Data:
        if i in Num:
            Sum = Sum + 1
            #i = i+ 1
    print(Sum)

def main():

    Size = int(input("Enter the Number of elements: "))

    Arr = list()

    print("Enter the elements: ")
    for i in  range(Size):
        no  = (input())
        Arr.append(no)


    t1 = threading.Thread(target=Small(Arr))

    t2 = threading.Thread(target=(Capital(Arr)))

    t3 = threading.Thread(target=Digits(Arr))



if __name__=="__main__":
    main()