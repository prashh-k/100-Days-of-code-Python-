

def word(s) :
    c = 0
    v = 0
    temp = False
    a = 0
    vowel = ["a","e","i","o","u"]
    hard = 0
    easy = 0
    for char in s :
        if char == " " :
            if temp == True or c > v :
                hard += 1
            else :
                easy += 1
            c = 0
            v = 0
            a = 0
            temp = False


        elif char in vowel :
            v += 1
            a = 0
        else :
            c += 1
            a += 1
            if a == 3 :
                temp = True

    if temp or c > v:
        hard += 1
    else:
        easy += 1

    q = (5 * hard) - (2 * easy)
    return q

str = input("Enter string : ")
print(word(str))