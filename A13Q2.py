

def AreaofCircle(r):
    pi = 3.14
    Area = pi*r*r
    return Area

#AreaofCircle = lambda pi,r,r : pi*r*r

def main():

    r = int(input("Enter radious: "))
    pi = 3.14
    Area = AreaofCircle(r)

    print("Area of Circle is: ",Area)

if __name__=="__main__":
    main()
