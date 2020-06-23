import random
def monopolyworp():
    aantalkeer = 0
    while True:
        input('Druk op enter om te goeien')
        dobbelsteen1 = random.randrange(1,7)
        dobbelsteen2 = random.randrange(1,7)
        if dobbelsteen1 == dobbelsteen2:
            if aantalkeer == 2:
                print(dobbelsteen1, '+', dobbelsteen2, '=', dobbelsteen1 + dobbelsteen2, '(Je hebt geluk)')
                break
            elif aantalkeer < 2:
                print(dobbelsteen1, '+', dobbelsteen2, '=', dobbelsteen1 + dobbelsteen2, '(Dubbel)')
                aantalkeer += 1
        else:
            print(dobbelsteen1,'+',dobbelsteen2,'=',dobbelsteen1+dobbelsteen2)
            break
monopolyworp()
