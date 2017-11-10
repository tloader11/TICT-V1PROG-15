leeftijd = eval(input("Geef je leeftijd: "))
paspoort = input("Nederlands paspoort: ")
if leeftijd >= 18 and paspoort == "ja":
    print("Je mag stemmen!")
else:
    print("Je mag niet stemmen.")
