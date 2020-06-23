def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt','r')
    regels = infile.readlines()
    kluizen = 0
    for i in regels:
        kluizen += 1
    kluizen = 12 - kluizen
    infile.close()
    return kluizen

def nieuwe_kluis():
    allekluizen = ['1','2','3','4','5','6','7','8','9','10','11','12']
    vulkluizen = []
    allekluizen2 = ''
    infile = open('kluizen.txt','r')
    regels = infile.readlines()
    if toon_aantal_kluizen_vrij() == 0:
        print('Er is momenteel geen beschikbare kluizen.')
    elif toon_aantal_kluizen_vrij() <= 12:
        for kluizen in regels:
            splitten = kluizen.split(';')
            vulkluizen.append(splitten[0])
        for kluis in vulkluizen:
            allekluizen.remove(kluis)
        for nummer in allekluizen:
            allekluizen2 += nummer + ', '
        kluisnummer = input('De beschikbare kluizen zijn : (' + allekluizen2 + '), kies maar een nummer van : ')
        infile.close()
        if kluisnummer in allekluizen:
            code = input('Voer uw code in (het moet tenminste 4 charachters zijn): ')
            if len(code) >= 4:
                outfile = open('kluizen.txt','r+')
                outfile.writelines(kluisnummer + ';' + code + '\n')
                outfile.writelines(regels)
                outfile.close()
                print('U kunt nu kluis nummer ' + kluisnummer + ' Gebruiken.')
            else:
                print('Uw code bestaat uit minder dan 4 charachters.')
        else:
            print('U heeft een onjuiste kluisnummer ingevoerd.')
    infile.close()

def kluis_openen():
    vulkluizen = []
    vulkluizencode = []
    infile = open('kluizen.txt', 'r')
    regels = infile.readlines()
    if toon_aantal_kluizen_vrij() >= 0:
        for kluizen in regels:
            splitten = kluizen.split(';')
            vulkluizencode.append(splitten[1])
            vulkluizen.append(splitten[0])
        kluisnummer = input('Voer uw kluisnummer in : ')
        if kluisnummer in vulkluizen:
            code = input('Voer uw code in : ')
            if  code+'\n' in vulkluizencode:
                if vulkluizen.index(kluisnummer) == vulkluizencode.index(code+'\n'):
                    resault = print('U heeft toegang naar uw kluis, het is nu open.')
                else:
                    resault = print('De compinatie van uw code en kluisnummer klopt niet')
            else:
                resault = print('De code klopt niet.')
        else:
            resault = print('U heeft een onjuiste kluisnummer ingevoerd.')
    else:
        resault = print('Er zijn geen vulle kluizen.')
    return resault

def kluis_teruggeven():
    wijziging = []
    vulkluizen = []
    vulkluizencode = []
    infile = open('kluizen.txt', 'r')
    regels = infile.readlines()
    infile.close()
    if toon_aantal_kluizen_vrij() >= 0:
        for kluizen in regels:
            splitten = kluizen.split(';')
            vulkluizencode.append(splitten[1])
            vulkluizen.append(splitten[0])
            wijziging.append(splitten)
        kluisnummer = input('Voer uw kluisnummer in : ')
        if kluisnummer in vulkluizen:
            code = input('Voer uw code in : ')
            if code + '\n' in vulkluizencode:
                if vulkluizen.index(kluisnummer) == vulkluizencode.index(code + '\n'):
                    wijziging.remove([kluisnummer, (code+'\n')])
                    outfile = open('kluizen.txt', 'w')
                    for i in wijziging:
                        outfile.write(i[0] + ';' + i[1])
                    outfile.close()
                    resault = print('U heeft toegang naar uw kluis, het is nu open, en het is beskhikbaar voor andere klanten.')
                else:
                    resault = print('De compinatie van uw code en kluisnummer klopt niet')
            else:
                resault = print('De code klopt niet.')
        else:
            resault = print('U heeft een onjuiste kluisnummer ingevoerd.')
    else:
        resault = print('Er zijn geen vulle kluizen.')
    return resault

while True:
    print('\n1: Ik wil weten hoeveel kluizen nog vrij zijn\n' +
          '2: Ik wil een nieuwe kluis\n' +
          '3: Ik wil even iets uit mijn kluis halen\n' +
          '4: Ik geef mijn kluis terug\n' +
          '5: Klaar\n')
    optie = int(input('Kies een optie bij alleen maar de nummer in te voeren: '))

    if optie == 1:
        if toon_aantal_kluizen_vrij() != 0:
            print('Het aantal beschikbare kluizen is : ' + str(toon_aantal_kluizen_vrij()))
        else:
            print('Er is momenteel geen beschikbare kluizen.')
    elif optie == 2:
        nieuwe_kluis()
    elif optie == 3:
        kluis_openen()
    elif optie == 4:
        kluis_teruggeven()
    elif optie == 5:
        print('Tot ziens...')
        break
    else:
        print('U heeft een onjoiste optie gekozen.')
