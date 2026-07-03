# for loop, , no append in list 
'''
def CheckFactor(no):
    Factor =[]
    for i in range(1,no+1):
        if no%i==0:
            Factor.append(i)
            i+1
    return Factor
'''
from MarvellousLibrary import CheckFactor

def main():
    Number = int(input("Enter Number: "))

    Ret = CheckFactor(Number)

    print("Factors of entered Number are: ",Ret)

if __name__=="__main__":
    main()