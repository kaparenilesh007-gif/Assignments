

import os


def main():

    fname  = input("Enter file name: ")

    if os.path.exists(fname):
        print("File present in CUrrent Directory")

    else:
        print("No such file available in cureent Directory")


if __name__=="__main__":
    main()