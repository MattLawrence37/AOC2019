startingNum = 235741;
endingNum = 706948;

def hasAdjacent(num):
    prevDigit = -1;
    for digit in str(num):
        if(digit == prevDigit):
            return True;
        else:
            prevDigit = digit;
    return False;

#This bit is horrible; I need to fix it up
def has2Adjacent(num):
    prevDigit = -1;
    hasDouble = False;
    digitCount = 0;
    for x in range(0, len(str(num)) -1):
        digit = str(num)[x];
        if(digit == prevDigit):
            digitCount = digitCount + 1;
            if(digit != str(num)[x+1] and digitCount == 1):
                hasDouble = True;
                digitCount = 0;
        elif(x == 4 and digit == str(num)[5]):
            return True;
        else:
            digitCount = 0;
        prevDigit = digit;
    return hasDouble;

def doesDecrease(num):
    prevDigit = -1;
    for digit in str(num):
        if(int(digit) < int(prevDigit)):
            return True;
        else:
            prevDigit = digit;
    return False;

matchCount = 0;
for num in range(startingNum, endingNum):
    if(has2Adjacent(num) and not doesDecrease(num)):
        print(num);
        matchCount = (matchCount + 1);

print(matchCount);
