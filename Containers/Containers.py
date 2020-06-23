import csv

with open('containers.csv','w',newline='') as myCSVFile:
    row = ('','Geordend','Muteerbaar','Iterable','Dubbele waarden toegestaan')
    column = ('Tuple','Dictionary','Set','List')
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(row)
    list = []
    klaar = True
    for type in column:
            for eigenschap in row[1:]:
                read = (input('Is '+type+' '+eigenschap+' ? (JA/NEE) ')).upper()

                if read == 'JA' or read == 'NEE':
                    list.append(read)
                    klaar = True
                else:
                    klaar = False
                    break
            if klaar == True:
                writer.writerow((type,list[0],list[1],list[2],list[3]))
                list.clear()
            else:
                print('U moet een waarde van (JA/NEE) met hoofdletters typen.')
                break
    myCSVFile.close()
