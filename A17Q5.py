

def main():

    Num = int(input("Enter possitive number: "))
    if Num >0:
        for i in range(2, Num):
            if Num % i ==0:
                print("Number is not Prime")
                break
        else:
            print("Number is Prime")
            
    else:
        print("Invalid number")

if __name__=="__main__":
    main()
