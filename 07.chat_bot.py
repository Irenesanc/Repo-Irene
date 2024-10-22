#Ask name
name= input ("Hi!, I`m a chat bot, what`s your name? ")
print("Nice to meet you",name)

#Ask birthday
year= int(input("What year where you born? "))
month=(input("In which month? "))
day= int(input("And day? "))

#Calculate the age; if the birthmonth is November or December (as we are still in October) then:
month_list=["November","December"]
if month in month_list:
    age=(2024-year-1)
    print("So you are",age)
else:
    age=(2024-year) 
    print("So you are",age)


#Ask hobbies
hobbies=input("What do you like to do in your free time? ")
print("Wow that hobbies sound really great, it was a pleasure to meet you!")