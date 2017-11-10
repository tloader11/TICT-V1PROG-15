getal = None
som = 0
counter = 0
while getal != 0:
    getal = eval(input("Geef een getal: "))
    som += getal
    counter+=1
print("Er zijn",counter-1,"getallen ingevoerd, de som is:",som)
