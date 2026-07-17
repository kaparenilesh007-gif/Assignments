'''
class : BankAccount

class veriable : RIO = 10.5

constructor = __init__ accepts Name and Amount

instance methods
Display() - Disaplay acc. holder's name and Current Balance
Deposit() - Accept an amount from user and add into balance
Withdraw() - Accept an amount from user and substarct from balance 
               (Ensure withdraw is allowed only if sufficient balance exist)
calculeateInterest() - calculate and returns interest using formula: Interest = (Amount *ROI)) 100

create multiple objects and demonstrate all methods

'''

class BankBalance:

    ROI = 10.5

    def __init__(self,Name,Amount):

        self.Name = Name
        self.AccBalance = Amount

    def Deposit(self):
        print("Enter Amount to deposit: ")
        DepAmount = int(input())
        self.AccBalance = self.AccBalance + DepAmount
        
        print("Available Balance is",self.AccBalance)
    
    def Withdraw(self):
        print("Enter Amount to withdraw: ")
        self.WithAmount = int(input())
    
        if self.WithAmount <= self.AccBalance:
            self.AccBalance = self.AccBalance - self.WithAmount
        else:
            print(f"please Enter amount below or equal to {self.AccBalance}")

        print("Available Balance is",self.AccBalance)

    def CalculateInterest(self):
        self.Interest = (self.AccBalance * BankBalance.ROI ) / 100
        print(f"Interst for your {self.AccBalance} is : ",self.Interest)

    def Display(self):
        print(f"Hello {self.Name} your available Amount is {self.AccBalance}")


obj = BankBalance("Akshada", int(10000))

obj.Display()
obj.Deposit()
obj.Withdraw()
obj.CalculateInterest()

        