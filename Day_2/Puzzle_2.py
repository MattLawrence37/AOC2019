file = open('input.txt', 'r')
mainListData = [];
for line in file.readlines():
    mainListData = line.rstrip().split(',');


calculated = False;
for noun in range(0, 99):
    if(calculated):
        break;
    for verb in range(0, 99):            
        mainListData = list(map(int, mainListData));

        listData = mainListData.copy();
        listData[1] = noun;
        listData[2] = verb;

        currentPos = 0;
        while(currentPos < len(listData)):
            opCode = listData[currentPos];
            if(opCode == 1):
                # Adds
                listData[listData[currentPos + 3]] = listData[listData[currentPos + 1]] + listData[listData[currentPos + 2]];
            elif(opCode == 2):
                # Multiplies
                listData[listData[currentPos + 3]] = listData[listData[currentPos + 1]] * listData[listData[currentPos + 2]];
            elif(opCode == 99):
                # Finishes
                break;
            else:
                print("Something went wrong...");
                break;

            currentPos += 4;

        if(listData[0] == 19690720):
            print("Program End");
            print(str(100 * noun + verb));
            calculated = True;
            break;

    
