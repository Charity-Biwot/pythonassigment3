# class Bank_name:
#     def __init__(self,deposit,balance,withdraw,account_number,name):
#         self.balance = balance+deposit - withdraw
#         self.deposit = deposit
#         self.withdraw = withdraw
#         self.account_number = account_number
#         self.name = name
        
#         def bank(self):
#             return f"Hello {self.name} your account number is {self.account_number} your deposit {self.deposit} and your withdrawal {self.withdraw} and your balance is {self.balance}"


class Account:
    def __init__(self,acc_number,name):
        self.balance = 0
        self.name = name
        self.acc_number =acc_number
        self.deposits=[]
        self.withdraws=[]
    
    

    def deposit(self,amount):
        if amount <=0:
            return f"Deposit amount should be more than zero"
        else:
            self.balance += amount
            self.deposits.append(self.balance)
            return f"You've deposited this amount {amount} and your balance is{self.balance}"
        
        
    def withdraw(self,amount):
        if amount > self.balance:
         return f"Your balance is {self.balance} you cannot withdraw the {amount}"
    
        elif amount <=0:
         return f"Amount must be greater than zero"

        else:
         self.balance -=amount
         self.withdraws.append(self.balance)
         return f"you have withdrawn {amount} your balance is {self.balance}"
     
    def deposits_statement(self):
         print(*self.deposits, sep="\n")
         
      
    def withdraws_statement(self):
         print(*self.withdraws, sep="\n")
     
     #Add a new attribute to the class Account called deposits which by default is an empty list.
#Add another attribute to the class Account called withdrawals which by default is an empty list.
#Modify the deposit method to append each successful deposit to self.deposits
#Modify the withdrawal method to append each successful withdrawal to self.withdrawals
#Add a new method called deposits_statement which prints each deposit in a new line
#dd a new method called withdrawals_statement which prints each withdrawal in a new line




             
