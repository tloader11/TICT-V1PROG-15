kosten = 4356
aantal_mensen = 0
try:
    aantal_mensen = int(input("Vul aantal mensen in: "))
except:
    print("Gebruik cijfers voor het invoeren van het aantal!")
    exit()

if(aantal_mensen == 0):
    print("Delen door nul kan niet!")
    exit()
elif(aantal_mensen < 0):
    print("Negatieve getallen zijn niet toegestaan!")
    exit()
try:
    per_persoon = kosten / aantal_mensen
    print("De kosten per persoon zijn €",per_persoon)
except:
    print("Onjuiste invoer!")
