import csv
bestand = '9_4.csv'
csvfile = open(bestand, 'w',newline='')
file = csv.writer(csvfile, delimiter=';')
file.writerow(("Artikelnummer", "Artikelcode", "Naam", "Voorraad", "Prijs"))
file.writerow((121,"ABC123", "Highlight pen", 231, 0.56 ))
file.writerow((123, "PQR678", "Nietmachine", 587, 9.99))
file.writerow((128, "ZYX163", "Bureaulamp", 34, 19.95))
file.writerow((137, "MLK709", "Monitorstandaard", 66, 32.50))
file.writerow((271, "TRS665", "Ipad hoes", 155, 19.01))
csvfile.close()
