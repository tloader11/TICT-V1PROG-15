cursisten = dict()
cursisten["bert"] = 3
cursisten["erik"] = 7
cursisten["bob"] =  4
cursisten["bill"] = 6.4
cursisten["rick"] = 9.1
cursisten["ashley"] = 9.2
cursisten["troll"] = 10
cursisten["bart"] = 1

for key in cursisten:
    if cursisten[key] > 9:
        print(key,"heeft een", cursisten[key], "gehaald!")
