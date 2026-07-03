def CheckGreater(V1, V2):
    if V1 > V2:
        print("No1 is Greater")
    else:
        print("No2 is Greater")
        

def main():
    No1 = int(input("Enter No: "))
    print("value of No1 is: ",No1)

    No2 = int(input("Enter No2: "))
    print("Value of No2 is: ",No2)

    CheckGreater(No1, No2)

if __name__ == "__main__":
    main()

'''
C:\Users\mp298\OneDrive - Cummins\Desktop\Python>python A9Q2.py
Enter No: 10
value of No1 is:  10
Enter No2: 20
Value of No2 is:  20
No2 is Greater
'''