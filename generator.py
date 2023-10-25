def isValid(national_code):
    digits = [int(digit) for digit in str(national_code).zfill(10)]
    if len(digits) != 10:
        return False
    else:
        sum = digits[0]*10 + digits[1]*9 + digits[2]*8 + digits[3]*7 + digits[4]*6 + digits[5]*5 + digits[6]*4 + digits[7]*3 + digits[8]*2
        rem = sum % 11
        if rem < 2:
            if digits[9] == rem:
                return True
        else:
            if digits[9] == (11-rem):
                return True
            else:
                return False