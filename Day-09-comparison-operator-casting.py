#comparison operator in  python 
# We can use various comparison operator in if statements other than just ==
# == : to check equality
# != : to check non equality
# < : check less than 
# > : check greater than 
# <= : check less than equal to
# >= : check greater than equal to 

#casting 

myScore = int(input("Your score: "))
if myScore >= 35 and myScore <= 100 :
  print("You are pass!")
elif myScore < 35 and myScore >= 0 :
  print("You are Fail!")  
else :
  print("Enter valid result you DUMB!")

#in above example when we try to use comparison operator with number and input data it throws error.

#cause  because the way input works behind the scenes is it always assumes what you are typing is text (or a string) and gets stored as a variable in "".

#Casting is where we explicitly tell the computer that what we are typing is a number and not a letter.

#here we are casting myScore variable input into int(), i.e  the variable, myScore will store the answer as a number.

myPi = float(input("What is Pi to 3dp? "))
if myPi == 3.142 :
  print("Exactly!")
else:
  print("Try again 😭")
  
# similarly we can use float() for floating number casting
# str() for string casting 

#challenge 

age = int (input("Enter Your Born Year : "))
if age >= 1925 and age <= 1946 :
  print("You are Tradionalists. ")
elif age >= 1947 and age <= 1964 :
  print("You are Baby Boomers. ")
elif age >= 1965 and age <= 1981 :
  print("You are Generation X. ")
elif age >= 1982 and age <= 1995 :
  print("You are Millenials. ")
elif age >= 1996 and age <= 2015 :
  print("You are Generation Z. ")
elif age >= 2016 and age <= 2023 :
  print("You are Generation Alpha. ")  
else :
  print("Enter correct choice.")
