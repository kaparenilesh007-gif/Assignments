
import sys


def main():

    Count = 0

    FileName = sys.argv[1]
    Parameter = sys.argv[2]

    with open(FileName,"r") as FileData:

        for Line in FileData:
            Word = Line.split()
            Count = Count + Word.count(Parameter)

        print(f"word '{Parameter}' avaible in this file {Count} time") #

if __name__=="__main__":
    main()