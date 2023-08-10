# Challenge 
name = input("Enter your name :")
profession = input("What do you do ? :")

if profession == "student" :
  print("Nice " + name +"Hope you are making progress as " + profession)
  feeling = input("How are you feeling now on scale of 1 to 10 ? :")
  if feeling == "1" or feeling == "2" or feeling == "3" or feeling == "4" or feeling == "5" :
    print("Don't feel low " + name + "You have to make more progress." )
  elif feeling == "6" or feeling == "7" or feeling == "8" or feeling == "9" or feeling == "10" :
    print("Nice to see " + name + "that you are that much motivated about it." )
  else :
    print("you Entered wrong Rating. ")
elif profession == "Teacher" :
  print("Nice to see we have some "+ profession + "also.")
  felling = input("How are you feeling now on scale of 1 to 10 ? :")
  if felling == "1" or felling == "2" or felling == "3" or felling == "4" or felling == "5" :
    print("Don't feel low " + name + " You have to make more progress." )
  elif felling == "6" or felling == "7" or felling == "8" or felling == "9" or felling == "10" :
    print("Nice to see " + name + " that you are that much motivated about it." )
  else :
    print("you Entered wrong Rating. ")
else :
  print("Entered Profession is not in data.")
    
    
