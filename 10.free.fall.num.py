#Define the variables (initial height, the gravity of the planet and the time)
h=float(input("Please enter the initial height(h): "))
g=float (input("Please enter the gravity of the planet(g): "))
t=((2*h)/g)**0.5

#Here I imported numpy and math for being able to do linspace
import numpy as np
import math

#I defined the time fractions in 5, putting as initial time 0 and final time (t)
time_fractions=np.linspace(0,t,5)
print(time_fractions)

#I calculated the distance in those times
distance_array= (h-(0.5)*g*time_fractions**2)
print(distance_array)

#Now I am going to calculate the average of these different positions.
average_positions=np.mean(distance_array)
print("The avegare positions of the object is:",average_positions)