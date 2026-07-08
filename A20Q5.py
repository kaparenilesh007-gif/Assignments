
import threading
import time

def Thread1(num):

    Numbers = []
    for i in range(1,num+1):
        Numbers.append(i)
    print(Numbers)

def Thread2(num):
    
    Rnumbers = []
    for i in range(num, 0, -1):
        Rnumbers.append(i)
    print(Rnumbers)


def main():

    Num = int(input("Enter Number: "))

    M_S_T = time.perf_counter()

    S_T = time.perf_counter()
    t1 = threading.Thread(target=Thread1(Num))
    t1.start()
    E_T = time.perf_counter()

    R_T = S_T - E_T
    print("For Thread1 time required: ",R_T)

    S_T = time.perf_counter()
    t2 = threading.Thread(target=Thread2(Num))
    t2.start()
    E_T = time.perf_counter()
    
    R_T = S_T - E_T
    print("For Thread2 time required: ",R_T)

    M_E_T = time.perf_counter()

    TimeRequired = M_S_T - M_E_T
    print ("Time Requred to run both Threads: ",TimeRequired)


if __name__=="__main__":
    main()

