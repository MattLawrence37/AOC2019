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

def GetOrbitalPath(planet, destination):
    visitedPlanets = [];
    prevOrbit = 0;
    currentOrbit = planet;
    while(currentOrbit != prevOrbit and currentOrbit != destination):
        found = False;
        visitedPlanets.append(currentOrbit);
        for orbit in orbits:
            if(found == True):
               break;
            for orbitals in orbits[orbit]:
                if(orbitals == currentOrbit):
                    prevOrbit = currentOrbit;
                    currentOrbit = orbit;
                    found = True;
                    break;
        if(found == False):
            break;
    return visitedPlanets;

youPath = list(reversed(GetOrbitalPath('YOU', 0)));
sanPath = list(reversed(GetOrbitalPath('SAN', 0)));
matchedOrbit = 0;
for x in range(0, len(youPath)):
    if(youPath[x] != sanPath[x]):
        matchedOrbit = youPath[x-1];
        break;

print(str(len(GetOrbitalPath('YOU', matchedOrbit))+len(GetOrbitalPath('SAN', matchedOrbit)) - 2));

