
from  _09_bank_account import Bank_Account  

#We welcome the user and ask for his/her number account
print("Welcome to the Chatbot Bank!")
number_account=int(input("Please enter your number account: "))
print("Hi, propietary of",number_account)


account=Bank_Account ("123456")

while True:
        #Now we ask the user what he would like to do
        command= input("What would you like to do? (deposit, withdraw, balance, exit): ")

        #If they want to deposit money, we will ask which amount
        if command=="deposit":
            amount=float(input("Please enter the amount you want to deposit: "))
            account.deposit (amount) #Here we are using the tool we had created in the class (Bank Account)
            print(f"You have deposited {amount} euros to your account. New balance:{account.get_balance()} euros.")
            #The new balance of the account is calculated by the "def" we had created before


         #If they want to withdraw money, we will ask which amount
        elif command=="withdraw":
            amount= float(input("Please enter the amount you want to withdraw of your account: "))
            account.withdraw(amount)
            if amount < account.get_balance():
                print(f"You have withdraw {amount} euros from your account. New balance: {account.get_balance()} euros.")
            else:
                print("Funds are insufficient.")

    
         #If the user wants to know which is theirs current balance of their account
        elif command=="balance":
            print(f"The current balance of the account is: {account.get_balance()} euros.")


        elif command=="exit":
            print("Thanks for trusting in Chat Bot account!")
            break #To exit the program 

    
        else:
            print("Im sorry I have not understand you, please try again.")


