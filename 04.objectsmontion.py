x0= float(input("Enter the initial position (x0): "))
v0= float(input( "Enter the initial velocity (v0): "))
t= float(input("Enter the time (t): "))
a= float (input("Enter the acceleration of the object (a): "))

x= x0+v0*t+0.5*a*t**2
v=v0+a*t

print ("The velocity of the object is:", v)
print ("The final position of the object is:",x)
print ("The acceleration of the object is: ",a)