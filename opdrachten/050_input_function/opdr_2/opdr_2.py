# Opdracht 2 berekeningen
# Naam student:
# Groep:


stop = True
gasten = ["rune", "paul", "kees", "marie", "hilda"]
while stop:
    tvvwst = (input("wil je een gast van of aan de lijst toevoegen of verwijderen? typ ""toevoegen"" of ""verwijderen"" wilt u stoppen typ ""stop"" \n"))

    if tvvwst== 'toevoegen':
        n_gast = input("voeg hier een gast toe \n")
        gasten.append(n_gast)
        print(gasten)

    if tvvwst== 'verwijderen':
        vw = input("typ hier de gast in die je wilt verwijderen\n")
        gasten.remove(vw)
        print(f"de gast is weggehaald hier is de nieuwe lijst {gasten}")

    if tvvwst== 'stop': 
        print (f"dit zijn alle gasten op de lijst {gasten}")
        stop = False
