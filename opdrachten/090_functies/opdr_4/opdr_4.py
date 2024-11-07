# Opdracht 1 functies
# Naam student:
# Groep:
def volledige_naam(lijst_met_namen):
    for naam in lijst_met_namen:
        # Voegt de volledige naam samen, maar alleen als tussenvoegsel niet leeg is
        volledige_naam = f"{naam['voornaam']} {naam['tussenvoegsel']} {naam['achternaam']}".strip()
        # Zorgt ervoor dat er geen dubbele spaties zijn door strip aan het einde toe te voegen
        print(' '.join(volledige_naam.split()))


namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

# Aanroep van de functie
volledige_naam(namen)
