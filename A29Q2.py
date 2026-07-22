import sys

def main():
    Fname = sys.argv[1]
    
    Fname = open(Fname,"r")
    data = Fname.read()
    print(data)

if __name__=="__main__":
    main()