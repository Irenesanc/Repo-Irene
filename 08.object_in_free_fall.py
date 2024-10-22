#Given constants
initial_height=float(input("Please, enter the initial height of the object (in meters): "))
gravity=float(input("Please, enter the gravity (in m/s**2): "))

#Having the initial height of the object and the gravity, we can calculate the time till the object`s final position=0 meters.
time=((2*initial_height)/gravity)**0.5

#Now, the maximum time means; the time till the objects touches the ground and the free fall ends.
print ("Knowing that the maximum time is",time )

#Ask (knowing that there is a maximum time) in which time you wanna know where the object is.
time_chosen= float(input("Enter the time of which you wanna know the position where the object is:" ))
position= 0,5*gravity*(time_chosen**2)

print("If time is",time_chosen)
print("The position of the object would be:",position)