# class Bank_name:
#     def __init__(self,deposit,balance,withdraw,account_number,name):
#         self.balance = balance+deposit - withdraw
#         self.deposit = deposit
#         self.withdraw = withdraw
#         self.account_number = account_number
#         self.name = name
        
#         def bank(self):
#             return f"Hello {self.name} your account number is {self.account_number} your deposit {self.deposit} and your withdrawal {self.withdraw} and your balance is {self.balance}"


from itertools import count
from selectors import SelectSelector


class Account:
    def __init__(self,acc_number,name):
        self.balance = 0
        self.name = name
        self.acc_number =acc_number
        self.deposits=[]
        self.withdraws=[]
        self_current =[]
    
    

    def deposit(self,amount):
        if amount <=0:
            return f"Deposit amount should be more than zero"
        else:
            self.balance += amount
            self.deposits.append(self.balance)
            return f"You've deposited this amount {amount} and your balance is{self.balance}"
        
        
    def withdraw(self,amount):
        count = 0
        if amount > self.balance:
         return f"Your balance is {self.balance} you cannot withdraw the {amount}"
    
        elif amount <=0:
         return f"Amount must be greater than zero"

        else:
         self.balance -=amount
         new_balance = self.balance-100
         self.withdraws.append(self.balance)
         print(self.withdraws)
         return f"you have withdrawn {amount} your balance is {self.balance}"
     
    def withdraws_statement(self):
         for i in self.withdraws:
             print(f"you have withdrawn {i}")
     
    
        
         
         
     
     #Add a new attribute to the class Account called deposits which by default is an empty list.
#Add another attribute to the class Account called withdrawals which by default is an empty list.
#Modify the deposit method to append each successful deposit to self.deposits
#Modify the withdrawal method to append each successful withdrawal to self.withdrawals
#Add a new method called deposits_statement which prints each deposit in a new line

#Modify the withdrawal method to include a transaction fee of 100 per transaction.
#Add a method to show the current balance



             
