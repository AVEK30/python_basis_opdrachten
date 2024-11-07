# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

leeftijdinput = int(input("Geef uw leeftijd in aantal jaar "))

def berekenkorting (leeftijdinput):
    for leeftijdscatogorie, (minleeftijd, maxleeftijd) in leeftijd.items():
        if minleeftijd <= leeftijdinput <= maxleeftijd:
            kortingspercentage = kortings_percentages[leeftijdscatogorie]
            prijskorting = normale_toegangsprijs * (1 - kortingspercentage / 100)
            print(f"U behoort tot de groep {leeftijdscatogorie}")
            print(f"U krijgt {kortingspercentage}% korting")
            print(f"U betaalt daarom {prijskorting:.2f}")
            return prijskorting

berekenkorting(leeftijdinput)

