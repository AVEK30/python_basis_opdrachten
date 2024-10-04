# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']


print(rivieren [0].title())#print de eerste rivier in de lijst met een hoofdletter.
print(rivier_info ["rijn"][1].title())#print het tweede land in de lijst van de rijn met een hoofdletter.

print(rivieren [1].title())#print de tweede rivier in de lijst met een hoofdletter.
print(rivier_info["maas"][0].title())#print het eerste land in de lijst van de maas met een hoofdletter.

print(rivieren [2].title())#print de derde rivier in de lijst met een hoofdletter.
print(rivier_info ["nijl"][2].title())#print het derde land in de lijst van de nijl met een hoofdletter.