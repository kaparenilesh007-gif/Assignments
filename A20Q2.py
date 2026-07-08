
import threading


def EvenFactor(num):
    Factors = []
    Sum = 0

    for i in range(2,num+1, 2):
        if num % i ==0:
            Factors.append(i)
    print(Factors)
    for i in Factors:
        Sum = Sum + i
    print("Addition of Even factors is: ",Sum)

def OddFactor(num):
    Factors = []
    Sum = 0

    for i in range(1,num+1, 2):
        if num % i !=0:
            Factors.append(i)
    print(Factors)

    for i in Factors:
        Sum = Sum + i
    print("Addition of odd factors is: ",Sum)

def main():
    Num = int(input("Enter Number: "))

    t1 = threading.Thread(target=EvenFactor(Num))
    
    t2 = threading.Thread(target=OddFactor(Num))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit From main")


if __name__=="__main__":
    main()