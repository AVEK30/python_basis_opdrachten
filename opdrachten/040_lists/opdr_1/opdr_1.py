# Opdracht 1 lists
# Naam student:
# Groep:

mylist = [] #maakt een nieuwe lijst aan
dict_1 = { "id": 0, "voornaam": "henk", "achternaam": "brouwer" }
dict_2 = { "id": 1, "voornaam": "guus", "achternaam": "gerritsen" }
dict_3 = { "id": 2, "voornaam": "philip", "achternaam": "zaaistra" }
dict_4 = { "id": 3, "voornaam": "liz", "achternaam": "van der kamp" }

#dit voegt alle dict's toe aan de lijst
mylist.append(dict_1)
mylist.append(dict_2)
mylist.append(dict_3)
mylist.append(dict_4)

print(mylist[1]["voornaam"], mylist[1]["achternaam"]) #print de voor en achternaam van lijst 2