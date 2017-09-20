file = open('Kaartnummers.txt','r')
grootste_nummer,regel_grootste_nummer,regelnummer = 0,0,0
for line in file.readlines():
    regelnummer +=1 #1 regel extra gelezen
    nummer = int(line.split(", ")[0])
    if grootste_nummer < nummer:
        grootste_nummer = nummer
        regel_grootste_nummer = regelnummer
print("Deze file telt {} regels".format(regelnummer))
print("Het grootste kaartnummer is: {} en dat staat op regel {}".format(grootste_nummer, regel_grootste_nummer))
