
from multiprocessing import Pool
import time



def Mult(List):

    Power1 = []
    for n in List:
        RaiseToFive = [n**5 for n in range(1, n + 1)]
        Power1.append(RaiseToFive)

    return Power1
    

def main():

    Numbers = [1000000,2000000,3000000,4000000]

    ST_ =time.perf_counter()

    with Pool(processes=4) as pool:

        Ret = pool.apply(Mult, args=(Numbers,))

    ET_ = time.perf_counter()

    RT_ = ET_ - ST_

    #print("power of number by 5 is: ",Ret)
    print(f"Total Time Required for execution is: {RT_}")

if __name__=="__main__":
    main()