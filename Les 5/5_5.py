def gemiddelde(text):
    stukjes = text.split(" ")
    i = 0
    total_wordlength = 0
    for word in stukjes:
        total_wordlength += len(word)
        i+=1
    print("De gemiddelde lengte van een woord is",round(total_wordlength/i),"characters lang")

gemiddelde("Dit is een test zin ditiseenlangwoord om te testen")
