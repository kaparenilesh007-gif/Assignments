
import sys
import os



def main():
    Afile = sys.argv[1]

    with open(Afile,"r") as Adata:
        Data = Adata.read()
    print(f"Data from first file: \n{Data}")

    with open("Demo.txt","w") as Bfile:
        Bfile.write(Data)

    with open("Demo.txt","r") as Cdata:
        Data2 = Cdata.read()
    print(f" Data from second files: \n{Data2}")
        
if __name__=="__main__":
    main()
