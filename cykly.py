# cyklus while - bežá dokud je splněna nějaká podmínka


#oko bere
from random import randrange
soucet = 0
while soucet < 21:
    print ("máš", soucet, "bodů")
    odpoved = input("chceš další kartu?")
    if odpoved == "ano":
        karta = randrange(2, 11,)
        print("otočil jsi", karta)
        soucet = soucet + karta
    elif odpoved == "ne":
        break
    else:
        print("Nerozumím, odpovídej ano a ne!")

if soucet == 21:
    print("Gratuluji, vyhrál jsi!")
elif soucet > 21:
    print("Smůla,", soucet, "je moc bodů")
else:
     print("Chybělo jen", 21 - soucet, "bodů")
