  # Grade Calculator

Sub = input("Enter Subject : ")
Max_marks = int(input("Enter Maximum Possible Marks :"))
Marks_got = int(input("Enter Marks You got: "))

percentage = round((Marks_got/Max_marks)*100 , 2) 
Grade  = ""
if percentage >= 90:
  grade = "A+"
elif percentage >= 80 :
  grade = "A-"
elif percentage >= 70 :
  grade = "B"
elif percentage >= 60 :
  grade = "c"
elif percentage >= 50 :
  grade = "D"
elif percentage >= 40 :
  grade = "U"

print(f"you got {Marks_got} out of {Max_marks} with {percentage} % in {Sub} Subject with grade of {grade}. ")