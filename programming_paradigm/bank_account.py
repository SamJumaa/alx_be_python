class Bank_Account:

    """Class representing bank_account"""

    def __init__(self, initial_balance):
        self._current_balance = initial_balance

    def deposit(self,amount):
        if amount > 0:
            self._current_balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self,amount):
        if amount <= self._current_balance :
            self._current_balance -= amount
            return True
         
        else:
            print("Insufficient funds")
            return False
        
       
    def display_balance (self):
        """Print the current acount balance."""
        print(f"The current account balance is: ksh {self._current_balance}")