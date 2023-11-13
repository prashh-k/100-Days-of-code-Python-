from getpass import getpass as input

player1 = input("Enter Your Choice :")
player2 =  input("Enter Yourb choice:")

if player1 == "rock" and player2 == "paper" :
  print("Player1 are been smothed by paper")
elif player1 == "scissor" and player2 == "rock" :
  print("Player1 is crushed by rock. ")
elif player1 == "paper" and player2 == "scissor" :
  print("player1 got cut by scissor")
elif player2 == "rock" and player1 == "paper" :
  print("Player2 are been smothed by paper")
elif player2 == "scissor" and player1 == "rock" :
  print("Player2 is crushed by rock. ")
elif player2 == "paper" and player1 == "scissor" :
  print("player2 got cut by scissor")
