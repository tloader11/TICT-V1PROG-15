def standaardprijs(afstandKM):
    prijs = 0
    if afstandKM > 50:
        prijs = 15 + (afstandKM-50)*0.60        #long ride
    elif afstandKM > 0:
        prijs = 0.80*afstandKM                  #normal method
    else:
        prijs = 0                               #negative number. ignore.
    return prijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    if weekendrit:
        if leeftijd < 12 or leeftijd >= 65:
            prijs = standaardprijs(afstandKM) * 0.65
        else:
            prijs = standaardprijs(afstandKM) * 0.60
    else:
        if leeftijd < 12 or leeftijd >= 65:
            prijs = standaardprijs(afstandKM) * 0.70
        else:
            prijs = standaardprijs(afstandKM)

    return '€ ' + str(round(prijs,2))


print(ritprijs(eval(input("Leeftijd: ")), eval(input("Weekendrit? ")), eval(input("Afstand in KM: "))))


