import random
import sys
getal = random.randint(1,100) #dit maakt verzint een random getal
raad = 0 
pogingen = 0 

while getal != raad:
    raad = (input("raad het getal: "))
    if str(raad) == ("stop"):
         quit()

    pogingen += 1
    if int(raad) > 100 or int(raad) < 0: #zorgd ervoor dat als je een getal boven 100 of onder 1 raad dat het programma stopt
        print("Ongeldige invoer druk op de any key om af te sluiten")
        input()
        quit()

    if int(raad) < getal: #verteld gebruiker of het geraden getal te hoog of te laag is
        print("te laag")
    elif int(raad) > getal:
        print("te hoog")
    else:
        print(f"ja geraden het koste je {pogingen} pogingen om te raden druk op de any key om af te sluiten")
        input()
        quit()

