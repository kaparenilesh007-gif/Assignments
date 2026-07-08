import sys

def CheckDiv5():
    
    Num = (int(sys.argv[1]))

    if Num %5==0:
        print("True")
  
    else:
        print("False")

CheckDiv5()