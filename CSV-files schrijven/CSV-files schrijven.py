import csv
import time
bestand = 'inloggers.csv'
achternaam_lijst=[]
with open(bestand,'r+',newline='') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')
    for find in reader:
        achternaam_lijst.append(find[2])
    while True:
        naam = input("Wat is je achternaam? ")
        if naam != 'end':
            voorl = input("Wat zijn je voorletters? ")
            gbdatum = input("Wat is je geboortedatum? ")
            email = input("Wat is je e-mail adres? ")
            if naam not in achternaam_lijst:
                achternaam_lijst.append(naam)
                persoon = (time.strftime("%a %d %b %Y") + ' at ' + time.strftime("%H:%M"),voorl,naam,gbdatum,email)
                writer = csv.writer(myCSVFile, delimiter=';')
                writer.writerow(persoon)
        else:
            myCSVFile.close()
            break
