file = open('input.txt', 'r')
planetData = [];
for line in file.readlines():
    planetData.append(line.rstrip().split(')'));

orbits = {};
for planet in planetData:
    if(planet[0] in orbits):
        orbits[planet[0]].append(planet[1]);
    else:
        orbits[planet[0]] = [planet[1]];

totalPlanets = [];
for orbit in orbits:
    currentOrbit = orbits[orbit];
    for planet in currentOrbit:
        if(planet not in totalPlanets):
            totalPlanets.append(planet);

totalOrbits = 0;
for x in range(0, len(totalPlanets)):
    prevOrbit = 0;
    currentOrbit = totalPlanets[x];
    while(currentOrbit != prevOrbit):
        found = False;
        for orbit in orbits:
            if(found == True):
               break;
            for orbitals in orbits[orbit]:
                if(orbitals == currentOrbit):
                    prevOrbit = currentOrbit;
                    currentOrbit = orbit;
                    found = True;
                    totalOrbits +=1;
                    break;
        if(found == False):
            break;

print(totalOrbits);
