file = open('input.txt', 'r')
listData = [];
for line in file.readlines():
    listData = line.rstrip().split(',');
	
listData = list(map(int, listData));
thrusters = [];

def opCodeComputer(thrusterNum, phase, signal):
    tempData = thrusters[thrusterNum][0];
    isPhase = True;
    currentPos = thrusters[thrusterNum][1];
    while(currentPos < len(tempData)):
        opCode = tempData[currentPos];

        immediateParam1 = False;
        immediateParam2 = False;

        if(opCode > 99):
            immediateParam1 = ((opCode // 100) % 10) == 1;
            immediateParam2 = ((opCode // 1000) % 10) == 1;
            opCode = opCode % 100;
        
        if(opCode == 1):
            # Adds
            param1 = tempData[currentPos + 1] if (immediateParam1 == True) else tempData[tempData[currentPos + 1]];
            param2 = tempData[currentPos + 2] if (immediateParam2 == True) else tempData[tempData[currentPos + 2]];
            tempData[tempData[currentPos + 3]] = param1 + param2;
            currentPos += 4;
        elif(opCode == 2):
            # Multiplies
            param1 = tempData[currentPos + 1] if (immediateParam1 == True) else tempData[tempData[currentPos + 1]];
            param2 = tempData[currentPos + 2] if (immediateParam2 == True) else tempData[tempData[currentPos + 2]];
            tempData[tempData[currentPos + 3]] = param1 * param2;
            currentPos += 4;
        elif(opCode == 3):
            # Sets value
            inputVal = signal;
            if(isPhase == True):
                inputVal = phase;
                isPhase = False;
            tempData[tempData[currentPos + 1]] = inputVal;
            currentPos += 2;
        elif(opCode == 4):
            thrusters[thrusterNum][1] = (currentPos + 2);
            # Prints value
            if(immediateParam1 == True):
                return tempData[currentPos + 1];
            else:
                return tempData[tempData[currentPos + 1]];
            currentPos += 2;
        elif(opCode == 5):
            # Jump if true
            param1 = tempData[currentPos + 1] if (immediateParam1 == True) else tempData[tempData[currentPos + 1]];
            if(param1 != 0):
                param2 = tempData[currentPos + 2] if (immediateParam2 == True) else tempData[tempData[currentPos + 2]];
                currentPos = param2;
            else:
                currentPos += 3;
        elif(opCode == 6):
            # Jump if false
            param1 = tempData[currentPos + 1] if (immediateParam1 == True) else tempData[tempData[currentPos + 1]];
            if(param1 == 0):
                param2 = tempData[currentPos + 2] if (immediateParam2 == True) else tempData[tempData[currentPos + 2]];
                currentPos = param2;
            else:
                currentPos += 3;
        elif(opCode == 7):
            # Less than
            param1 = tempData[currentPos + 1] if (immediateParam1 == True) else tempData[tempData[currentPos + 1]];
            param2 = tempData[currentPos + 2] if (immediateParam2 == True) else tempData[tempData[currentPos + 2]];
            if(param1 < param2):
                tempData[tempData[currentPos + 3]] = 1;
            else:
                tempData[tempData[currentPos + 3]] = 0;
            currentPos += 4;
        elif(opCode == 8):
            # Equal to
            param1 = tempData[currentPos + 1] if (immediateParam1 == True) else tempData[tempData[currentPos + 1]];
            param2 = tempData[currentPos + 2] if (immediateParam2 == True) else tempData[tempData[currentPos + 2]];
            if(param1 == param2):
                tempData[tempData[currentPos + 3]] = 1;
            else:
                tempData[tempData[currentPos + 3]] = 0;
            currentPos += 4;
        elif(opCode == 99):
            thrusters[thrusterNum][1] = currentPos;
            # Finishes
            return -2;
            print("Program End");
            break;
        else:
            print("Something went wrong");
    return -1;
    print("END");

sequence = [5];
for num in range(6, 10):
    tempSequence = [];
    for com in sequence:
        for pos in range(0, len(str(com)) + 1):
            tempSequence.append(str(com)[:pos] + str(num) + str(com)[pos:]);
    sequence = tempSequence;


for x in range(0, 5):
    thrusters.append(listData.copy());

highestSignal = 0;
for order in sequence:
    thrusters.clear();
    for x in range(0, 5):
        thrusters.append([listData.copy(), 0, 0]);
    
    signal = 0;
    i = 0;
    for phase in [int(x) for x in str(order)]:
        signal = opCodeComputer(i, phase, signal);
        i += 1;
        if(signal > highestSignal):
            highestSignal = signal;
    shouldContinue = True;
    while(shouldContinue == True):
        i = 0;
        for phase in [int(x) for x in str(order)]:
            signal = opCodeComputer(i, signal, signal);
            if(signal == -2):
                shouldContinue = False;
                break;
            i += 1;
            if(signal > highestSignal):
                highestSignal = signal;
        
print(highestSignal);
    
