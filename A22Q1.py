
from multiprocessing import Pool
import time



def Mult(List):

    Power1 = []
    for n in List:
        sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6
        Power1.append(sum_of_squares)

    return Power1
    

def main():

    Numbers = [1000000,2000000,3000000,4000000]

    with Pool(processes=4) as pool:

        Ret = pool.apply(Mult, args=(Numbers,))


    print("sqaure of entedred Number is: ",Ret)
    

if __name__=="__main__":
    main()