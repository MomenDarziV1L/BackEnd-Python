kost = 2356
aantal = input('De hotel huur kost €'+str(kost)+', voer het aantal rezigers in: ')
try:
    if int(aantal) > -1: # ik heb hier -1 gebruikt om te laten zien wat geat gebeuren als de gebruiker 0 heeft ingevoerd
        persoon_kost = kost/int(aantal)
        print('Elke persoon betaalt: €'+str(persoon_kost))
    else:
        print('Negatieve getallen zijn niet toegestaan!')
except ValueError:
    print('Gebruik cijfers voor het invoeren van het aantal!')
except ZeroDivisionError:
    print('Delen door nul kan niet!')
except:
    print('Onjuiste invoer!')
