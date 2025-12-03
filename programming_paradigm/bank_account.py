class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self,amount):
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self,amount):
        if amount <= self._account_balance :
            self._account_balance - = amount
            return True
         
        else:
            print("Insufficient funds")
            return False
        
       
    def display_balance (self):
        """Print the current acount balance."""
        print(f"The current account balance is: ksh {self._account_balance}")