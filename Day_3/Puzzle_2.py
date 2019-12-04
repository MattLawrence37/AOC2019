import math;

file = open('input.txt', 'r')
wires = [];
for line in file.readlines():
    currWire = line.rstrip().split(',');
    wires.append(currWire);

wireCoords = [];

for wire in wires:
    wireData = [[0,0]];
    for x in wire:
        prevData = wireData[len(wireData) - 1];
        direction = x[0];
        count = int(x[1:]);
       
        if(direction == "U"):
            wireData.append([prevData[0], prevData[1] - count]);
        elif(direction == "D"):
            wireData.append([prevData[0], prevData[1] + count]);
        elif(direction == "L"):
            wireData.append([prevData[0] - count, prevData[1]]);
        elif(direction == "R"):
            wireData.append([prevData[0] + count, prevData[1]]);                      
        else:
            print("Something went wrong");

    wireCoords.append(wireData);

def distance(coord1, coord2):
    return math.sqrt(((coord1[0]-coord2[0])**2)+((coord1[1]-coord2[1])**2));

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return 0;

    d = (det(*line1), det(*line2))
    x = int(det(d, xdiff) / int(div))
    y = int(det(d, ydiff) / int(div))
    if(distance(line1[0], [x,y]) + distance(line1[1], [x,y]) == distance(line1[0], line1[1])):
        if(distance(line2[0], [x,y]) + distance(line2[1], [x,y]) == distance(line2[0], line2[1])):
            return x, y
    return 0;

intersections = [];
for x in range(0, len(wireCoords[0]) - 1):
    coord1 = wireCoords[0][x];
    coord2 = wireCoords[0][x+1];
    for y in range(0, len(wireCoords[1]) - 1):
        coord3 = wireCoords[1][y];
        coord4 = wireCoords[1][y+1];
        intersectCoords = line_intersection([coord1, coord2], [coord3, coord4]);
        if(intersectCoords != 0):
            intersections.append(intersectCoords);

#this here is all so gross, but it works
intersectDictOne = {};
intersectDictTwo = {};
for sect in intersections:
    intersectDictOne[str(sect)] = 0;
    intersectDictTwo[str(sect)] = 0;

totalDistance = 0;
for x in range(0, len(wireCoords[0]) - 1):
    coord1 = wireCoords[0][x];
    coord2 = wireCoords[0][x+1];
    for sec in intersectDictOne:
        if(intersectDictOne[sec] == 0):
            targetCoord = [int(s) for s in sec.strip("() ").split(',')];
            if(distance(coord1, targetCoord) + distance(coord2, targetCoord) == distance(coord1, coord2)):
                intersectDictOne[sec] = totalDistance + distance(coord1, targetCoord);
    totalDistance = totalDistance + distance(coord1, coord2);

totalDistance = 0;
for x in range(0, len(wireCoords[1]) - 1):
    coord1 = wireCoords[1][x];
    coord2 = wireCoords[1][x+1];
    for sec in intersectDictTwo:
        if(intersectDictTwo[sec] == 0):
            targetCoord = [int(s) for s in sec.strip("() ").split(',')];
            if(distance(coord1, targetCoord) + distance(coord2, targetCoord) == distance(coord1, coord2)):
                intersectDictTwo[sec] = totalDistance + distance(coord1, targetCoord);
    totalDistance = totalDistance + distance(coord1, coord2);
    
for sec in intersectDictTwo:
    dist1 = int(intersectDictOne[sec]);
    dist2 = int(intersectDictTwo[sec]);

    total = dist1+dist2;
    intersectDictOne[sec] = total;

lowestDistance = -1;
for sect in intersectDictOne:
    i = intersectDictOne[sect];
    if(i > 0 and (lowestDistance == -1 or i < lowestDistance)):
        lowestDistance = i;

print("lowest " + str(lowestDistance));

    




