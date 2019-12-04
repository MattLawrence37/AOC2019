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
    if(hasAdjacent(num) and not doesDecrease(num)):
        matchCount = (matchCount + 1);

print(matchCount);
