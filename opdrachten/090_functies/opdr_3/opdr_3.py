import math

def kubus_vol(m):
    # Bereken het volume van een kubus met zijde m
    volume = m ** 3
    return volume

def bol_vol(r):
    # Bereken het volume van een bol met straal r
    volume = (4/3) * math.pi * (r ** 3)
    return volume

# Voorbeelden
zijde = 5
radius = 4

print(f"De inhoud van de kubus met zijde {zijde} is: {kubus_vol(zijde)}")
print(f"De inhoud van de bol met straal {radius} is: {bol_vol(radius)}")
