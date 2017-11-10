__author__ = 'Tristan'
import random
config = 'kluizen_config.txt'

def claim_locker():
    with open(config, 'r') as file :
        filedata = file.read()
    for line in open(config, 'r'):
        combi = line.split(" ")
        locker_no = combi[0]
        locker_code = combi[1]
        print(locker_no,locker_code)
        if("----" in locker_code):
            code = ""
            for i in range(4):
                code += ""+str(random.randrange(1,10))
            print("kluis nummer:", locker_no, "met code:", code)
            filedata = filedata.replace(str(locker_no)+" ----", str(locker_no)+" "+str(code))

            writeback = open(config,'w')
            writeback.write(filedata)
            writeback.flush()
            writeback.close()
            return
    print("Geen lege kluis beschikbaar!")

def open_locker():
    nummer = input("Vul uw kluisnummer in: ")
    for line in open(config, 'r'):
        combi = line.split(" ")
        if(nummer == combi[0]):
            code = combi[1]
            ingevoerd = input("Voer uw code in: ")
            if(code[:4]==ingevoerd+""):
                print("Locker open!")
            else:
                print("Verkeerde code!")

def release_locker():
    nummer = input("Vul uw kluisnummer in: ")
    for line in open(config, 'r'):
        combi = line.split(" ")
        if(nummer == combi[0]):
            code = combi[1]
            ingevoerd = input("Voer uw code in: ")
            if(code[:4]==ingevoerd+""):
                file = open(config, 'r')
                nconf = file.read()
                nconf = nconf.replace(nummer + " " + code, nummer + " ----\n")
                writefile = open(config,'w')
                writefile.write(nconf)
                writefile.flush()
                writefile.close()
                print("Kluisje vrijgegeven!")
            else:
                print("Verkeerde code!")

def free_lockers():
    nummers = []
    for line in open(config, 'r'):
        combi = line.split(" ")
        if("----" in combi[1]):
            nummers.append(combi[0])
    print("De vrije kluisjes zijn: ",nummers)

def keuze_menu():
    print("====================================")
    print("1: Ik wil een nieuwe kluis")
    print("2: ik wil mijn kluis openen")
    print("3: Ik geef mijn kluis terug")
    print("4: Ik wil weten hoeveel kluizen er nog vrij zijn")
    keuze = int(input("Maak een keuze (1,2,3,4): "))
    if(keuze == 1):
        claim_locker()
    elif(keuze == 2):
        open_locker()
    elif(keuze == 3):
        release_locker()
    elif(keuze == 4):
        free_lockers()

while(True):
    keuze_menu()