import csv
file = open('9_3_gamers.csv', 'r')
reader = csv.reader(file, delimiter=';')
highscore = 0
name = ""
time = ""
for rule in reader:
    if int(rule[2]) > highscore:
        highscore = int(rule[2])
        name = rule[0]
        time = rule[1]
print("De hoogste score is: {} op {} behaald door {}".format(highscore,time,name))
