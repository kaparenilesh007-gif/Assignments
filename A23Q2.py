
from multiprocessing import Pool
import os



def CheckOdd(List):

    print(f"PID of Factorial1: {os.getpid()} Input Number: {List}")
    Sum = 0
    for i in range(2, List + 1):

        if i % 2 != 0:

            Sum = Sum + i
    return Sum
    

def main():

    Numbers = [1000000,2000000,3000000,4000000]

    with Pool(processes=4) as pool:

        Ret = pool.map(CheckOdd,Numbers)


    print("Sum of Odd Numbers of each data is: ",Ret)
    

if __name__=="__main__":
    main()