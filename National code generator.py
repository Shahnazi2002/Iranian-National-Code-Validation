from random import randint
def vailNationalCode(n):
    digits = list(map(int, f"{n}"))
    length = len(digits)==10
    if length == True :
        validity = (digits[0]*10) + (digits[1]*9) + (digits[2]*8) + (digits[3]*7) + (digits[4]*6) + (digits[5]*5) + (digits[6]*4) + (digits[7]*3) + (digits[8]*2)
        remainder = validity%11
        if remainder == 0 :
            if digits[9] == 0 :
                return True
            else:
                return False
        elif remainder == 1 or remainder == 10 :
            if digits[9] == 1 :
                return True
            else:
                return False
        elif remainder == 2 :
            if digits[9] == 9 :
                return True
            else:
                return False
        elif remainder == 3 :
            if digits[9] == 8 :
                return True
            else:
                return False
        elif remainder == 4 :
            if digits[9] == 7 :
                return True
            else:
                return False
        elif remainder == 5 :
            if digits[9] == 6 :
                return True
            else:
                return False
        elif remainder == 6 :
            if digits[9] == 5 :
                return True
            else:
                return False
        elif remainder == 7 :
            if digits[9] == 4 :
                return True
            else:
                return False
        elif remainder == 8 :
            if digits[9] == 3 :
                return True
            else:
                return False
        elif remainder == 9 :
            if digits[9] == 2 :
                return True
            else:
                return False
    else:
        return False

repeat = True
while repeat :
    generated = randint(0,10000000000)
    if vailNationalCode(generated) :
        print(generated)
        repeat = False