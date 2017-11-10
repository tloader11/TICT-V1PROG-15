def namen():
    namenlijst = dict()
    while True:
        naam = input("Volgende naam: ").lower().capitalize()
        if(naam == ""): break
        if(namenlijst.get(naam) != None):
            namenlijst[naam] += 1
        else: namenlijst.setdefault(naam,1)
    for key in namenlijst:
        if namenlijst[key] == 1:
            print("Er is 1 student met de naam",key)
        else:
            print("Er zijn",namenlijst[key],"studenten met de naam",key)
            
namen()
