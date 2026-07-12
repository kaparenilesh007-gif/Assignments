
import multiprocessing


def CheckPrimeN(Data):
    
        count = 0

        for num in range(2, Data + 1):
            Prime = True
            for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        Prime = False
                        break
            if Prime == True:
                count = count + 1

        print(count)

def main():
     

    
    MP1 = multiprocessing.Process(target=CheckPrimeN, args=(10000,))
    MP2 = multiprocessing.Process(target=CheckPrimeN, args=(20000,))
    MP3 = multiprocessing.Process(target=CheckPrimeN, args=(30000,))
    MP4 = multiprocessing.Process(target=CheckPrimeN, args=(40000,))

    MP1.start()
    MP2.start()
    MP3.start()
    MP4.start()

    MP1.join()
    MP2.join()
    MP3.join()
    MP4.join()
    
     
if __name__=="__main__":
     main()
