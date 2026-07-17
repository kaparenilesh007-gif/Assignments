
'''
create class: Demo
one class veriable: Value
Define Constructor: (__init__)
constructor accepts two parameters and initializes the instance veriable 
two instance veriables: no1, no2
implement two instance methods:
  Fun() - display the value of veriable no1 and no2
  Gun() - display the value of veriable no1 and no2

  Create two objects of Demo class
  obj1 = Demo(11, 21)
  obj2 = Demo(51, 101)

  call the instance method as below

  obj1.Fun()
  obj2.Fun()
  obj1.Gun()
  obj2.Gun()

'''

class Demo:

    Value = 0

    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B
        
    def Fun(self):
        print(self.no1, self.no2)

    def Gun(self):
        print(self.no1, self.no2)


obj1 = Demo(11, 21)
obj2 = Demo(51, 101)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()