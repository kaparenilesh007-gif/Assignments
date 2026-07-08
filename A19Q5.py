'''
Filter list condition: with prime Numbers

map the filtered paramater Condition: multiply each parameter by 2 

reduce the maped list COndition: Max paramater from maped data 

'''
from functools import reduce

def CheckPrimeN(num):

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

        return True

Increament = lambda no1: (no1*2)


def main():

    NumberOfInputs = int(input("Enter Number of Inputs: "))

    Data = []
    for i in range (1,NumberOfInputs+1):
        D1 = (int (input("Enter Data: ")))
        Data.append(D1)

    Fdata = list(filter(CheckPrimeN ,Data))
    print(Fdata)

    Mdata = list(map(Increament,Fdata))
    print(Mdata)

    Rdata = reduce(max, Mdata)
    print(Rdata)

if __name__=="__main__":
    main()


    