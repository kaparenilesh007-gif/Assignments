


import sys
import os


def main():

    FileName = sys.argv[1]
    Parameter = sys.argv[2]

    with open(FileName,"r") as FileData:
        Data = FileData.read()
        if Parameter in Data:
            print(f"word '{Parameter}' avaible in this file ")
        else:
            print(f"{Parameter} word Not avaible in this file")

if __name__=="__main__":
    main()