def code(invoerstring):
    uitvoer = ""
    for c in invoerstring:
        uitvoer += chr(ord(c)+3)
    return uitvoer
print(code("RutteAlkmaarDen Helder"))
