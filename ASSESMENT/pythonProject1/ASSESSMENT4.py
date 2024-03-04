class Bank_account:
    def __init__(self,name,account_no,balance,date_of_opening):
        self.name =name
        self.account_no = account_no
        self.balance =balance
        self.date_of_opening =date_of_opening
class Deposit(Bank_account):
    def __init__(self,name,account_no,amount_to_deposit,):
        super().__init__(name,account_no)
        self.balance += amount_to_deposit
class Withdrawal(Deposit):
    def __init__(self,name,account_no,withdrawal):
        super().__init__(name,account_no)
        self.balance += withdrawal
