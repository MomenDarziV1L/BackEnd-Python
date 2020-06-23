gebruiker = 'momen'
wachtwoord = '123456'
mobielenummer = '06421745'
while True:
    print('\n1- Mobielenummer wijzigen\n2- Inloggegevens wijzigen')
    optie = input('\nKies een optie bij alleen maar de nummer ervan te typen: ')
    if optie == '1' or optie == '2':
        gebruiker2 = input('\nVoor de gebruikersnaam in: ')
        wachtwoord2 = input('Voor de wachtwoord in: ')
        if wachtwoord == wachtwoord2 and gebruiker == gebruiker2:
            if optie == '1':
                print('\nDe huidige mobiele nummer is : '+mobielenummer)
                mobielenummer2 = input('Voer de nieuwe mobielenummer in of laat het maar leeg als u geen wijziging wil doen: ')
                if mobielenummer2 != '':
                    mobielenummer = mobielenummer2
                    print('\nDe mobielenummer is gewijzigd!!')
                else :
                    print('\nDe mobielenummer blijft de zellfde!!')
            elif optie == '2':
                print('\nAls u niet meer de inloggegevens wilt wijzigen, laat ze maar leeg.')
                gebruiker2 = input('Voor de nieuwe gebruikersnaam in: ')
                wachtwoord2 = input('Voor de nieuwe wachtwoord in: ')
                if gebruiker2 != '' and wachtwoord2 != '':
                    wachtwoord = wachtwoord2
                    gebruiker = gebruiker2
                    print('\nDe inloggegevens zijn gewijzigd')
        else:
            print('\nDe inloggegevens zijn niet juist.')
            #Stuur een brief dat iemand aan het proberen is om inteloggen
    elif optie=='quit':
        break
