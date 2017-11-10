import csv
bestand = '9_4.csv'
csvfile = open(bestand, 'r',newline='')
file = csv.reader(csvfile, delimiter=';')
firstRow = True
duurst = 0
voorraad = -1
duurst_id = 0
vorraad_id = 0
counter = 0
items = []
totaal_voorraad = 0
for rule in file:
    if firstRow:
        firstRow = False
    else:
        if float(rule[4]) > duurst:
            duurst = float(rule[4])
            duurst_id = counter
        if float(rule[3]) < voorraad or voorraad==-1:
            voorraad = float(rule[3])
            vorraad_id = counter
        items.append(rule)
        totaal_voorraad+=int(rule[3])
        counter +=1
print("Het duurste artikel is {} en die kost {} Euro".format(items[duurst_id][2],duurst))
print("Er zijn slechts {} exemplaren in voorraad van het product met nummer {}".format(voorraad,items[vorraad_id][0]))
print("In totaal hebben wij {} producten in ons magazijn liggen".format(totaal_voorraad))

csvfile.close()
