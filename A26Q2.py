
class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print("Enter Radius")
        self.Radius = int(input())

        #print(self.Radius)
        return self.Radius

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius* self.Radius

        #print(self.Area)
        return self.Area

    def CalculateCircumference(self):
        self.Circumference = (2* (Circle.PI))* self.Radius

        #print(self.Circumference)
        return self.Circumference

    def Display(self):
        print("Inside Display")
        print(f"Entered Radius is: {self.Radius}")
        print(self.Area)
        print(self.Circumference)

obj = Circle()

obj.Accept()
obj.CalculateArea()
obj.CalculateCircumference()
obj.Display()

