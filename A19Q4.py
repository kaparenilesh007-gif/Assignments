'''
Filter list condition: with even parameters

map the filtered paramater Condition: sqare of filtered list

reduce the maped list COndition: Addition of all maped parameters 

'''
from functools import reduce

CheckEven = lambda no: no%2==0

Increament = lambda no1: (no1**2)

Product = lambda no1, no2 : no1 + no2


def main():

    NumberOfInputs = int(input("Enter Number of Inputs: "))

    Data = []
    for i in range (1,NumberOfInputs+1):
        D1 = (int (input("Enter Data: ")))
        Data.append(D1)

    Fdata = list(filter(CheckEven ,Data))
    print(Fdata)

    Mdata = list(map(Increament,Fdata))
    print(Mdata)

    Rdata = reduce(Product, Mdata)
    print(Rdata)

if __name__=="__main__":
    main()