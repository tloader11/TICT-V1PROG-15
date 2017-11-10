stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard", "Maastricht"]
def inlezen_beginstation(stations):
    invoer = input("Vul beginstation in: ")
    while invoer not in stations: invoer = input("Vul beginstation in: ")
    return invoer
def inlezen_eindstation(stations, beginstation):
    invoer = input("Vul eindstation in: ")
    while invoer not in stations: invoer = input("Vul eindstation in: ")
    eindindex = stations.index(invoer)
    beginindex = stations.index(beginstation)
    if eindindex <= beginindex:
        print("U moet een station invoeren dat NA het startstation ligt.")
        return inlezen_eindstation(stations,beginstation)
    return invoer
def omroepen_reis(stations, beginstation, eindstation):
    begin_index = stations.index(beginstation) + 1
    eind_index = stations.index(eindstation) + 1
    print("U begint op station {}. Deze heeft een index van {}\nU eindigt op station {}. Deze heeft een index van {}".format(beginstation,begin_index,eindstation,eind_index))
    print("De afstand van de reis (in stations) is {}.\nDe ritprijs is {}".format(eind_index-begin_index,(eind_index-begin_index)*5))
    print("Jij stapt in de trein in: "+beginstation)
    for i in range(begin_index,eind_index-1):
        print("     -"+stations[i])
    print("Jij stapt uit in: "+eindstation)

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations,beginstation,eindstation)
