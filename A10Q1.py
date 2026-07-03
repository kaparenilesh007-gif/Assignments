def Table(no):
    i = 1
    Arr = list()
    while(i <= 10):
        no1 =no * i
        no = no
        i= i+1
        Arr.append(no1)
    return(Arr)
        

def main():
    No1 = int(input("Enter Number: "))
    
    Ret = Table(No1)
    print("Table of entered number is: ",Ret)



if __name__=="__main__":
    main()
