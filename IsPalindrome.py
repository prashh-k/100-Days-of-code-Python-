def isPalindrome(s):
    return s == s[::-1]

s = input("Enter")
if isPalindrome(s) == 0:
    print(0)
else :
    print (1)