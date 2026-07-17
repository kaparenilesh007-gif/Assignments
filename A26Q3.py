

class Arithmetic:


    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
        self.Add = 0
        self.Sub = 0
        self.Mult = 0
        self.Div = 0

    def Accept(self):
        print ("Enter First Number: ")
        self.Value1 = (int(input()))

        print ("Enter Second Number: ")
        self.Value2 = (int(input()))
 

    def Addition(self):
        self.Add = self.Value1 + self.Value2

        print(self.Add)  
    
    def Substraction(self):
        self.Sub = self.Value1 - self.Value2

        print(self.Sub)

    def Multiplication(self):
        self.Mult = self.Value1 * self.Value2

        print(self.Mult)

    def Division(self):
        if self.Value2 >=1:
            self.Div = self.Value1 / self.Value2

        else:
            print("Can not devide by Zero")

        print(self.Div)
        

obj = Arithmetic()

obj.Accept()
obj.Addition()
obj.Substraction()
obj.Multiplication()
obj.Division()