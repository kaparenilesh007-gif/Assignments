

import sys
import os


def main():

    FileName = sys.argv[1]

    #FileName = open(FileName,"r")
    with open(FileName,"r") as FileData:
        for Lines in FileData:
            print(Lines, end="")
    

if __name__=="__main__":
    main()
