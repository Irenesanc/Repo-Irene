# Monthly Loan Payments variables:

import pandas as pd

#P is the principal loan ammount
P=float(input("Enter the principal loan ammount: "))
#r is the monthly interest rate
r=float(input("Enter the monthly interest rate (annual interest divided by 12 months): "))
#n is the loan termns
n=float(input("Enter the loan terms (in months): "))

rango_n=range(1,n+1)

#Monthly Loan Payments`s formula`
M= (P*(r*(1+r)**n))/((1+r)**n-1)

payments_df=pd.DataFrame({'Month':rango_n,'Payment': M})
print(payments_df)

Total_payment=M*n
print("Total payment is",Total_payment)
print("The monthly payment is:",M)

