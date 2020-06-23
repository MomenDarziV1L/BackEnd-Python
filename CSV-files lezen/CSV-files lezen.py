import csv
with open('gamers.csv','r',newline='') as myCSVFile:
    gamers = []
    hoosgte_score=[]
    reader = csv.reader(myCSVFile, delimiter=';')
    for gamer in reader:
        gamers.append(gamer)
        hoosgte_score.append(int(gamer[2]))
    for gamer in gamers:
        if int(gamer[2]) == max(hoosgte_score):
            print('De hoogste score is:', gamer[2], 'op', gamer[1], 'behaald door', gamer[0])