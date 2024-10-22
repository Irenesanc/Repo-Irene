# Monthly Loan Payments variables:

#P is the principal loan ammount
P=float(input("Enter the principal loan ammount: "))
#r is the monthly interest rate
r=float(input("Enter the monthly interest rate (annual interest divided by 12 months): "))
#n is the loan termns
n=float(input("Enter the loan terms (in months): "))

#Monthly Loan Payments`s formula`
M= (P*(r*(1+r)**n))/((1+r)**n-1)

print("The monthly payment of the loan is:",M)
