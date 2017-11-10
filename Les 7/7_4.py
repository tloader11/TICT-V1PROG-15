def ticker(filename):
    file = open(filename,"r")
    returndict = dict()
    for line in file.readlines():
        line = line[:-1] #remove \n
        returndict[line.split(":")[0]] = line.split(":")[1]
    return returndict


print( ticker("7_4_ticker.txt") )
