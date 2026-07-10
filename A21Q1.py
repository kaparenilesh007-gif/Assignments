

import threading

def Prime(Data):
        
    Prime_List = []
    
    for num in Data:
        isPrime = True
        for i in range(2, int(num **0.5)+1):
              if num% i == 0:
                   isPrime = False
                   break
        if isPrime:
            Prime_List.append(num)
    print(Prime_List)
    

def NonPrime(Data):
     
        NonPrime_List = []
        for num in Data:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    NonPrime_List.append(num)
                    break
        print(NonPrime_List)

def main():

    Size = int(input("Enter the Number of elements: "))

    Arr = list()

    print("Enter the elements: ")
    for i in  range(Size):
        no  = int(input())
        Arr.append(no)


    t1= threading.Thread(target=Prime, args=(Arr,))
    t2 = threading.Thread(target=NonPrime, args=(Arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    main()