# Operators

adding = 4 + 3
print(adding)

subtraction = 8 - 9
print(subtraction)

multiplication = 4 * 32
print(multiplication)

division = 50 / 5
print(division)

# a number raised to the power of some number
# in this example we raise 5 to the power of 2
squared = 5**2
print(squared)

# remainder of a division
modulo = 15 % 4
print(modulo)

# whole number division
divisor = 15 // 2
print(divisor)


#Bill Splitter and challenge

myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = int(input("What % of tip you are giving us ? : "))
totalBill = myBill + (myBill * tip) /100 ;

answer = totalBill / numberOfPeople
round(answer, 2)
print("You all owe", answer)