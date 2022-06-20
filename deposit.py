class Bank:
    def __init__(self,acc_no,name,balance,deposit,withdrawals):
        self.balance = balance + deposit -withdrawals
        self.name = name
        self.acc_no = acc_no

def bank(self):
    return f"Hello {self.name } your account is {self.acc_no}  and your balance is {self.balance}"

class Account:
    def __init__(self,acc_no,name):
        self.acc_no = self.acc_no
        self.balance = 0
        self.deposits = []
        self.withdrawals =[]
        self.current = []

        def deposit(self,amount):
            if amount <=0:
                return f"amount should be more than zero"
            else:
                self.balance +=amount
                self.deposits.append(self.balance)
                return f"you have deposited {self.deposits} and your balance is {self.balance}"

            def withdrawals(self,amount):
                count = 0












