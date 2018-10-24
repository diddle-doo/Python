from abc import ABCMeta,abstractmethod
from random import randint
class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount(self):
        return 0
    @abstractmethod
    def authenticate(self):
        return 0
    @abstractmethod
    def withdraw(self):
        return 0
    @abstractmethod
    def deposit(self):
        return 0
    @abstractmethod
    def displayAvaialableBalance(self):
        return 0

class Savings(Account):
    def __init__(self):
        # [key][0]=>name ; [key][1]=>balance
        self.savingsAccount={}

    def createAccount(self,name,initialDeposit):
        self.accountNumber= randint(10000,99999)
        self.savingsAccount[self.accountNumber]=[name,initialDeposit]
        print("Your Account was successfully created!  Your Account Number is : ", self.accountNumber)

    def authenticate(self,name,accountNumber):
        if accountNumber in self.savingsAccount.keys():
            if self.savingsAccount[accountNumber][0]==name:
                print("Authentication is successful")
                self.accountNumber=accountNumber
                return True
            else:
                print("Authentication failed")
                return False
        else:
            print("Authentication failed")

    def withdraw(self,withdrawAmount):
        if withdrawAmount > self.savingsAccount[self.accountNumber][1]:
            print("Insufficient balance")
        else:
            self.savingsAccount[self.accountNumber][1] =- withdrawAmount
            print("Withdraw successful")
            self.displayAvaialableBalance()

    def deposit(self,depositAmount): # update
        self.savingsAccount[self.accountNumber][1]=+depositAmount
        print("Deposit was successful")
        self.displayAvaialableBalance()


    def displayAvaialableBalance(self):
        print("Available balance",self.savingsAccount[self.accountNumber][1])

savingsAccount=Savings()
while True:
    print()
    print("Enter 1 to create a new account")
    print("Enter 2 to access existing account")
    print("Enter 3 to exit")
    userChoice=int(input())
    if userChoice==1:
        print("Enter your name: ")
        name=input()
        print("Enter your intial amount")
        intialAmount=int(input())
        savingsAccount.createAccount(name,intialAmount)
    elif userChoice==2:
        print("Enter your name")
        name=input()
        print("Enter your account number")
        accountNumber=int(input())
        authenticationStatus=savingsAccount.authenticate(name,accountNumber)
        if authenticationStatus is True:
            while True:
                print()
                print("Enter 1 to withdraw amount")
                print("Enter 2 to deposit")
                print("Enter 3 to display")
                print("Enter 4 to main menu")
                userChoice=int(input())
                if userChoice is 1:
                    print("Enter the amount you wish to withdraw")
                    withdrawAmount=int(input())
                    savingsAccount.withdraw(withdrawAmount)
                elif userChoice is 2:
                    print("Enter the amount you wish to deposit")
                    depositAmount=int(input())
                    savingsAccount.deposit(depositAmount)
                elif userChoice is 3:
                    savingsAccount.displayAvaialableBalance()
                elif userChoice is 4:
                    break
    elif userChoice is 3:
            quit()

