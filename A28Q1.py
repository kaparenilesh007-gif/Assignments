
import sys

def main():
    FileName = sys.argv[1]

    with open(FileName, "r") as File:
        Lines = len(File.readlines())
    print(f"Total lines are: {Lines}")

if __name__=="__main__":
    main()
