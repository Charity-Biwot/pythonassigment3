 #Add a new attribute to the class Account called deposits which by default is an empty list.
#Add another attribute to the class Account called withdrawals which by default is an empty list.
#Modify the deposit method to append each successful deposit to self.deposits
#Modify the withdrawal method to append each successful withdrawal to self.withdrawals
#Add a new method called deposits_statement which prints each deposit in a new line

#Modify the withdrawal method to include a transaction fee of 100 per transaction.
#Add a method to show the current balance
from datetime import datetime

# class Bank_name:

#     def __init__(self,deposit,balance,withdraw,account_number,name):
#          self.balance = balance+deposit - withdraw
#          self.deposit = deposit
#          self.withdraw = withdraw
#          self.account_number = account_number
#          self.name = name
        
#          def bank(self):
#              return f"Hello {self.name} your account number is {self.account_number} your deposit {self.deposit} and your withdrawal {self.withdraw} and your balance is {self.balance}"


from itertools import count
from selectors import SelectSelector
from datetime import datetime
#            #quiz4
#Add a new attribute loan_balance which is zero by default.

class Account:
    def __init__(self,acc_number,name):
        self.balance = 0
        self.name = name
        self.acc_number =acc_number
        self.deposits=[]
        self.withdraws=[]
        self_current =[]
        self.loan_balance = 0
         
    ##Update the withdrawal method to store each withdrawal transaction 
# as a dictionary like like this 
#{
#"date": datetime object,
#"amount": amount,
#"narration": deposit or withdrawal
#} 
    

    def deposit(self,amount):
        if amount <=0:
            return f"Deposit amount should be more than zero"
        else:
            saved = {"date":datetime.now().strftime("%d,%m,%y"),"amount":amount,"narration":f"Thankyou for depositing{amount},at {datetime.now()}"}
            self.deposits.append(saved)
            self.balance += amount
            self.deposits.append(self.balance)
            return f"You've deposited this amount {amount} and your balance is,{self.balance}"
        
     
    def withdraw(self,amount):
        count = 0
        if amount > self.balance:
         return f"Your balance is {self.balance} you cannot withdraw the {amount}"
    
        elif amount <=0:
         return f"Amount must be greater than zero"

        else:
         details ={"date":datetime.now().strftime("%d,%m,%y"),"amount":amount,"narration":f"Thankyou for depositing{amount},on {datetime.now()}"}
         self.withdraws.append(details) 
         self.balance -=amount
         self.transaction = self.balance-100
         self.withdraws.append(self.balance)
         print(self.withdraws)
         return f"you have withdrawn {amount} your balance is {self.balance}"
     
    def withdraws_statement(self):
         for n in self.withdraws:
             print(f"you had withdrawn {n}")
             
    def deposits_statement(self):
        for x in self.deposits:
            print(f"you have deposited {x}")
            
    def current_statement(self):
        for y in self.current_statement:
            print(f"your current balance is {y}")
    ##quiz3
#Add a new method  full_statement which combines both deposits and withdrawals 
# into one list ordered by date and using a for loop prints each transaction 
# in a new line like this
#16/06/22 —----- Deposit —---- 1000
    def full_statement(self):
        z = self.deposits + self.withdraws
        for i in z:
            print(i)
            
 #quiz5
#Add a borrow method which allows a customer to borrow if they meet these conditions:
#Customer has made at least 10 deposits.
#Loan amount requested must be more than 100
#A customer qualifies for a loan amount that is less than  or equal to 1/3 of their total sum of deposit history
#Customer account has no  balance
#Customer has no outstanding loan
#The loan attracts  an interest of 3%.      
    def borrow (self,amount):
        if len(self.deposits)<10:
            return f"Add more deposits" 
        if amount<100:
            return f" Inquire for more than 100 loan"  
        for x in self.deposit:
            sum=0
            sum+=x["amount"]  
        if amount>sum/3:
            return f"Dear {self.name} you can borrow money up to {sum/3}" 
        if self.balance!=0:
            return f"Dear {self.name} you still have balance of {self.balance}" 
        if self.loan_balance!=0:
            return f"Dear {self.name} you still have the balance of {self.loan_balance}"
        if self.balance!=0:
            return f"Dear {self.name} you still  have balance of {self.balance}" 
        if self.loan_balance !=0:
            return f"Dear {self.name} you still have the balance of {self.loan_balance}, hence repay to borrow" 
        else:
            interest= amount*0.03
            self.loan_balance+=amount+interest
            return f"Dear {self.name} you have borrowed {self.loan_balance} and your balance is {self.balance}"
#Add a loan repayment method with these conditions
#A customer can repay a loan to reduce the current loan balance
#Overpayment of a loan increases a customers current deposit


    def loan_repayment(self,amount):
        if amount<0:
            return f"Amount is invald"
        if amount > self. loan_balance:
            self.balance += amount-self.loan_balance
            return f"Dear {self.name} thank you for repaying your load of {amount-self.loan_balance} and your account  balance is {self.balance}"
        else:
            self.loan_balance-=amount
            return f"Dear {self.balance} thank you, you've loan of {amount} and your current loan balance is {self.loan_balance}"
        #Add a new method transfer which accepts two attributes (amount and instance of another account).
        # If the amount is less than the current instances balance, 
        # the method transfers the requested amount from the current 
        # account to the passed account. The transfer is accomplished by 
        # reducing the current account balance and depositing the requested
        # amount to the passed account.


    def transfer(self,amount,instance_account):
        if amount<=0:
            return f"invalid"
        if amount>= self.balance:
            return f"insufficient amount in your account"
        if isinstance(instance_account,Account):
            self.balance-=amount
            instance_account.balance += amount
            return f"you have transfered {amount} to {instance_account} account with the name {instance_account.name} and your new balance is {self.balance}"
            
   
        
            
                   



     




               



    
    
    
        
         
         
     
    


             
