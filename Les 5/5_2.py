file = open('Kaartnummers.txt','r')
nummers = file.readlines()
for nummer in nummers:
    delen = nummer.split(", ")
    print("{} heeft het kaartnummer: {}".format(delen[1].strip(),delen[0]))
