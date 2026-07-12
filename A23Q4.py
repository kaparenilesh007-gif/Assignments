

import os
#import threading
from multiprocessing import Pool
import math


def Factorial1(no):
    print(f"PID of Factorial1: {os.getpid()} Input Number: {no}")
    
    Fact = []
    for i in no:
        Fact.append(math.factorial(i))
    return Fact


def main():

    Numbers = [10,15,20,25]
    
    with Pool(processes=4) as pool:

        Fact = pool.apply(Factorial1, args=(Numbers,))

    print("Factorial of Number is:", Fact)

if __name__=="__main__":
    main()