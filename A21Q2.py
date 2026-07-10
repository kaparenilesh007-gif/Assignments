
import threading


def MaxNum(list1):

    Maximum = max(list1)

    print("Maximum Number is: ",Maximum)

def MinNum(list2):

    Minimum = min(list2)

    print("Minimum Number is: ",Minimum)


def main():

    Size = int(input("Enter the Number of elements: "))

    Arr = list()

    print("Enter the elements: ")
    for i in  range(Size):
        no  = int(input())
        Arr.append(no)


    t1 = threading.Thread(target=MaxNum, args=(Arr,))
    t2 = threading.Thread(target=MinNum, args=(Arr,))

    t1.start()
    t2.start()
 
    t1.join()
    t2.join()

if __name__=="__main__":
    main()