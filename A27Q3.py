

class Numbers:

    def __init__(self,value):
        self.Value = value

    def ChkPrime(self):

        Count = 0
        for i in range(2,self.Value):
            if self.Value % i == 0:
                Count +=1

        if Count == 0:
            print("Entered Number is Prime")
        else:
            print("Entered Number is NOT Prime")

    def CheckPerfect(self):

        Perfect = []
        Perfect2 = 0
        for i in range(1,self.Value):
            if self.Value % i == 0:
                Perfect.append(i)
        print(Perfect)

        Perfect2 = sum(Perfect)
        if Perfect2 == self.Value:
            print("Entered Number is Perfect")
        else:
            print("Entered Number is NOT Perfect")


    def Factors(self):

        Facts = []

        for i in range(1,self.Value):
            if self.Value % i == 0:
                Facts.append(i)
                i = i + 1

    def SumOfFactors (self):

        Facts = []

        for i in range(1,self.Value):
            if self.Value % i == 0:
                Facts.append(i)
                i = i + 1

        FactSum = sum(Facts)
        print("Sum of Factors of Entered Number is: ",FactSum)


obj = Numbers(555555)

obj.ChkPrime()
obj.CheckPerfect()
obj.Factors()
obj.SumOfFactors()

