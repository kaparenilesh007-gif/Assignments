
import sys

def main():
    File_1 = sys.argv[1]
    File_2 = sys.argv[2]

    with open(File_1,"r") as F1:
        Data_1 = F1.read()
        #print(Data_1)
        #return(Data_1)

    with open(File_2,"r") as F2:
        Data_2 = F2.read()
        #print(Data_2)
        #return(Data_2)
    
    if Data_1 == Data_2:
        print(f"Same Content in file {File_1} and {File_2}")
    else:
        print("Not same Content ")
    


if __name__=="__main__":
    main()