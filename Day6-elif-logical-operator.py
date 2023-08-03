#elif statements 
# we can have as many as elif statement as we want but they should be in between if and else.

# username = input("Enter Your  Name: ")

# if username == "Marks" :
#   print("Welcome Marks !! ")
# elif username == "Prash" :
#   print("Welcome Prash !!")
# elif username == "Harry" :
#   print("welcome Harry !!")
# else :
#   print("GO AWAY !!")



# using logical operator 

username = input("Enter Your  Name: ")
password = input("Enter Your Password: ")

if username == "Marks" and password =="Mark@123" :
  print("Welcome Marks")
elif username == "Prash" and password =="Prash@123" :
  print("Welcome Prash !!")
elif username == "Harry" and password =="@Harry123" :
  print("welcome Harry !!")
else :
  print("GO AWAY !!")