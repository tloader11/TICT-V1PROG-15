def kwadraten_som(grondgetallen):
    som = 0
    for grondgetal in grondgetallen:
        if grondgetal > 0:
            som += grondgetal*grondgetal
    return som

print(kwadraten_som([3,5,4,-9,-5]))
