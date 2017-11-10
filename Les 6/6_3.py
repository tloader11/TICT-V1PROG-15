invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
getallen = invoer.split("-")
getallen.sort()
for i in range(0,len(getallen)):
    getallen[i] = int(getallen[i])
print("Gesorteerde list van ints:",getallen)
print("Het grootste getal is",invoer[-1],"en het kleinste getal is",invoer[0])
print("Aantal getallen:", len(getallen) ,"en Som van de getallen:", sum(getallen))
print("Gemiddelde:",sum(getallen) / len(getallen))
