#We create a class to define a bank account.
class Bank_Account:
    
    #The bank account has an account number and an inicial balance (it starts by default in 0)
    def __init__(self,account_number):
        self.account_number= account_number 
        self.balance= 0 

    #Now, with "deposit", we will be able to deposit money into the account, so the current balance should increase.
    def deposit(self,amount):
        self.balance +=amount

    #The withdraw action is for substracting money from the account.
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print ("The account has insuficient funds.")

    #Get balance is for returning the current balance.
    def get_balance (self):
        return self.balance
    
    #String representation of the account when it is printed
    def __str__(self):
        return f"Account number: {self.account_number}, Balance: {self.balance}"


#INSTANCE OF A BANK ACCOUNT:

#First of all, we name our account:
account_1= Bank_Account ("123456")

#Now, we will deposite some money (for example 1000 euros):
account_1.deposit (1000)
print(account_1)

#Right now, lets try withdraw some money (for example 500 euros):
account_1.withdraw(500)
print(account_1)

#To finish the example, we are going to try withdraw more money than we have in the account:
account_1.withdraw(5000)
print(account_1)