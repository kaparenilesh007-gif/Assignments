
RectangleArea = lambda Lenght, Width: Lenght * Width

def main():
    Length = int(input("Enter Lenght: "))
    Width = int(input("Enter Width: "))
    Area = RectangleArea(Length,Width)
    print("Area of Rectangle is: ",Area)

if __name__=="__main__":
    main()

