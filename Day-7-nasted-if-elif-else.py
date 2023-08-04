#Nesting 
#Nesting is where we put an if statement within an if statement using the power of indenting.
#The second if statement within the first if statement must be indented and its print statement needs to be indented one more time.


# tvShow = input("What is your favorite tv show? ")
# if tvShow == "peppa pig":
#   print("Ugh, why?")
#   faveCharacter = input("Who is your favorite character? ")
#   if faveCharacter == "daddy pig":
#     print("Right answer")
#     villen = input("Who is villen in show :")
#     if villen == "monkey" :
#       print ("your correct.")
#     else :
#       print ("you are wrong") 
#   else:
#     print("Nah, Daddy Pig's the greatest")
# elif tvShow == "paw patrol":
#   print("Aww, sad times")
# else:
#   print("Yeah, that's cool and all…")

#challenge 

print ("Fake Fan Finder  ")
print ("****************")
anime = input("Name of your anime :")
if anime == "one piece" :
  print("Awesome!")
  character = input ("Who is favourite character ? (luffy, zoro, sanji) : ")
  if character == "luffy" :
    print("You are lucky.")
    luffy = input("Bounty of  luffy ?")
    if luffy == "3 biLlion" :
      print("You are True Fan !!")
    else :
        print("You are NOT True Fan !!")
  elif character == "zoro" :
    print("You are lucky.")
    zoro = input("What is name of sword which zoro got in wano ?")
    if zoro == "enma" or zoro == "ichimonji" or zoro == "kitetsu III" :
      print("You are True Fan !!")
    else :
        print("You are NOT True Fan !!")
  elif character == "sanji"   :
    print("You are lucky.")
    sanji = input("Sanji's other name :")
    if sanji == "black foot sanji" :
      print("You are True Fan !!")
    else :
        print("You are NOT True Fan !!")  
  
else :
  print("Your choose different anime.")