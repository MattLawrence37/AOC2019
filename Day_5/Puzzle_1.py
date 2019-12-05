file = open('input.txt', 'r')
listData = [];
for line in file.readlines():
    listData = line.rstrip().split(',');
	
listData = list(map(int, listData));

currentPos = 0;
while(currentPos < len(listData)):
    opCode = listData[currentPos];

    immediateParam1 = False;
    immediateParam2 = False;
    #immediateParam3 = False;

    if(opCode > 99):
        immediateParam1 = ((opCode // 100) % 10) == 1;
        immediateParam2 = ((opCode // 1000) % 10) == 1;
        #immediateParam3 = ((opCode // 10000) % 10) == 1;
        opCode = opCode % 100;
    
    if(opCode == 1):
        # Adds
        param1 = listData[currentPos + 1] if (immediateParam1 == True) else listData[listData[currentPos + 1]];
        param2 = listData[currentPos + 2] if (immediateParam2 == True) else listData[listData[currentPos + 2]];
        listData[listData[currentPos + 3]] = param1 + param2;
        currentPos += 4;
    elif(opCode == 2):
        # Multiplies
        param1 = listData[currentPos + 1] if (immediateParam1 == True) else listData[listData[currentPos + 1]];
        param2 = listData[currentPos + 2] if (immediateParam2 == True) else listData[listData[currentPos + 2]];
        listData[listData[currentPos + 3]] = param1 * param2;
        currentPos += 4;
    elif(opCode == 3):
        # Sets value
        listData[listData[currentPos + 1]] = int(input("Enter number for address " + str(listData[currentPos + 1]) + ": "));
        currentPos += 2;
    elif(opCode == 4):
        # Sets value
        print("Address " + str(listData[currentPos + 1]) + " contains value: " + str(listData[listData[currentPos + 1]]));
        currentPos += 2;
    elif(opCode == 99):
        # Finishes
        print("Program End");
        break;
    else:
        print("Something went wrong");

    
