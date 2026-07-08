'''
Filter list condition: parameter >=70 and number <= 90

map the filtered paramater Condition: increase each by 10

reduce the maped list COndition: product of all maped parameters 

'''
from functools import reduce

CheckWithin = lambda no: no>=70 and no<=90

Increament = lambda no1: (no1+10)

Product = lambda no1, no2 : no1*no2

def filterX(Task, Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)                            
        if Ret == True:
            Result.append(no)
    return Result


def main():

    NumberOfInputs = int(input("Enter Number of Inputs: "))

    Data = []
    for i in range (1,NumberOfInputs+1):
        D1 = (int (input("Enter Data: ")))
        Data.append(D1)

    Fdata = list(filterX(CheckWithin,Data))
    print(Fdata)

    Mdata = list(map(Increament,Fdata))
    print(Mdata)

    Rdata = reduce(Product, Mdata)
    print(Rdata)

if __name__=="__main__":
    main()