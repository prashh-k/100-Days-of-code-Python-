# Python3 program to find largest number
# divisible by 90 that can be made
# using 0 and 5

# from math import every methods
from math import *

# Function to find largest number
# divisible by 90 that can be made
# using 0 and 5
def printLargestDivisible(a) :

	# Count of 0s and 5s
	c0, c5 = 0, 0

	for i in range(len(a)) :

		if a[i] == 0 :
			c0 += 1
		else :
			c5 += 1

	# The number of 5s that can be used
	c5 = floor(c5 / 9) * 9

	if c0 == 0 : # The number can't be
		print(-1,end = "") # made multiple of 10

	elif c5 == 0 : # The only multiple of 90
		print(0,end = "") # that can be made is 0

	else :

		for i in range(c5) :
			print(5,end = "")
		for i in range(c0) :
			print(0, end = "")



# # Driver code
# if __name__ == "__main__" :
#
# 	a = [ 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5]
# 	n = len(a)
#
# 	# Function calling
# 	printLargestDivisible(n, a)
#
# # This code is contributed by
# # ANKITRAI1


inp = input()
list_inp = inp.split(",")
int_list_inp =[int(item) for item in list_inp]
print(list_inp)
print(int_list_inp)
print(printLargestDivisible(int_list_inp))