#Criterios para aprobar/suspender

exam_score= float(input("Enter the exam score of the student (0-100): "))
number_of_clases= int(input("Enter the number of clases of the course: "))
number_of_clases_attended= int (input("Enter the number of clases attended by the student: "))

if exam_score>=70 and number_of_clases_attended>=(80*number_of_clases)/100:
    print("The student has pass physics.")
else:
    print ("The student has fail physics.")
