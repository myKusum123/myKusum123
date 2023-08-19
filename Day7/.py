'''Write a program to create the class "Account "with following data property and data method
data property : account name, balance;
data method : deposite(),withdraw()& Inquery(0)
The data property must be initialixzed through constuctor
test the above class by creating two objects and perform deposite , withdraw and inquery operation
'''
class Account:
    accountName=str()
    balance=float()
    def __init__(self,an,b):
        self.accountName=an
        self.balance=b
        print(f"Dear{an},your account is created")
    def deposite(delf,am):
        if am>0:
            self.balance +=0
            print(f"amount+{am}, is deposited")
        else:
            print("invalid amount")
    def withdraw(self,am):
          if self.balance>=am:
            self. balance-=am
            print(f'{am}is withdraw')
          else:
            print("insufficient amount")
    
    def inquery(self):
        print(f'your balance is{self.balance}')

    # home work =theprogramminghub.com-courses-python-python conditional statement-python loop