# Opdracht 1 condities
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

# Hier start de for-loop....

looplist = []
for x in range(1,11):
    looplist.append(x)

looplist4 = [i for i in looplist if i > 4]
print(looplist4)