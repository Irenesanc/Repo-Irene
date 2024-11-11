from _09_bank_account import Bank_Account

#Here I create the first child account (SavingsAccount)
class SavingsAccount (Bank_Account):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        #Aply the interest to the account.
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: {interest} euros. New balance: {self.balance} euros")

    def estimate_interest(self, months):
        #Estimate the interest earned in a given period.
        future_balance = self.balance * ((1 + self.interest_rate) ** months)
        estimated_interest = future_balance - self.balance
        print(f"Estimated interest after {months} months: {estimated_interest:.2f} euros")
        return estimated_interest

    def __str__(self):
        #Savings Account Representation
        return f"Savings Account - {super().__str__()}, Interest Rate: {self.interest_rate * 100}%"
    
#Now I`m going to create the second child account (CheckingAccount)
class CheckingAccount(Bank_Account):
    def __init__(self, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        #Withdraw from the account taking into account the overdraft limit
        if amount > 0 and self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}euros. New balance: {self.balance} euros.")
        else:
            print("Insufficient funds or overdraft limit exceeded.")

    def set_overdraft_limit(self, new_limit):
        #Set a new overdraft limit
        if new_limit >= 0:
            self.overdraft_limit = new_limit
            print(f"Overdraft limit set to ${new_limit}.")
        else:
            print("Overdraft limit cannot be negative.")

    def __str__(self):
        #Current Account Representation
        return f"Checking Account - {super().__str__()}, Overdraft Limit: ${self.overdraft_limit}"