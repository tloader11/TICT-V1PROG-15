def WordOfFourInList(list):
    resultlist = []
    for word in list:
        if len(word) == 4: resultlist.append(word)
    print("De nieuw-gemaakte lijst met alle vier-letter strings is:\n",resultlist)

WordOfFourInList(eval(input("Geef lijst met minimaal 10 strings: ")))
