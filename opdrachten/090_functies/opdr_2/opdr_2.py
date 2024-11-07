# Opdracht 1 functies
# Naam student:
# Groep:


def kilometers_naar_miles(km):
    return km / 1.609344


def miles_naar_kilometers(miles):
    return miles * 1.609344

kilometers = 1223
miles = 867

milesc = kilometers_naar_miles(kilometers)
kmc = miles_naar_kilometers(miles)

print(f"{kilometers} kilometers = {milesc} ")
print(f"{miles} miles = {kmc}")