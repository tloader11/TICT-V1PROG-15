import datetime
import csv
bestand = '9_2_inloggers.csv'
while True:
    csvfile = open(bestand, 'a',newline='')
    file = csv.writer(csvfile, delimiter=';')
    naam = input("Wat is je achternaam? ")
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")
    date = datetime.datetime.today().strftime("%a %d %b %Y at %H:%M")
    print(([date, voorl, naam, gbdatum, email]))
    file.writerow((date, voorl, naam, gbdatum, email))
    csvfile.close()


