import csv
lijst = [('Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs'),
         ('121', 'ABD123', 'Highlight pen', '231', '0.56'),
         ('123', 'PQR678', 'Nietmachine', '587', '9.99'),
         ('128', 'ZYX163', 'Bereaulamp', '34', '19.95'),
         ('137', 'MLK709', 'Monitorstandaard', '66', '32.50'),
         ('271', 'TRS665', 'Ipad hoes', '155', '19.01')]

with open('headers.csv','w',newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    for row in lijst:
        writer.writerow(row)
    myCSVFile.close()

with open('headers.csv','r',newline='') as myCSVFile:
    totaal = 0
    duur = {}
    kleinste_voorraad = {}
    reader = csv.DictReader(myCSVFile, delimiter=';')
    for product in reader:
        try:
            if float(product['Prijs']) > float(duur['Prijs']):
                duur.update(product)
        except KeyError:
            duur.update(product)
        try:
            if int(product['Voorraad']) < int(kleinste_voorraad['Voorraad']):
               kleinste_voorraad.update(product)
        except KeyError:
            kleinste_voorraad.update(product)
        totaal += int(product['Voorraad'])
    print('Het duurste artikel is',duur['Naam'],'en die kost',duur['Prijs'],'Euro')
    print('Er zijn slechts',kleinste_voorraad['Voorraad'],'exemplaren in voorraad van het product met nummer',kleinste_voorraad['Artikelnummer'])
    print('In totaal hebben wij',totaal,'producten in ons magazijn liggen')
    myCSVFile.close()