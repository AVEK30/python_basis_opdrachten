party = []

voorn = input("wat is je voornaam?\n")
with open ("input.txt", "w") as file:
    file.write(voorn + "\n")

achtern = input("wat is je achternaam?\n")
with open ("input.txt", "a") as file:
    file.write(achtern + "\n")

drank = input("wat voor drank neem je mee?\n")
with open ("input.txt", "a") as file:
    file.write(drank + "\n")

eten = input("wat neem je mee om te eten?\n")
with open ("input.txt", "a") as file:
    file.write(eten + "\n")


print("\nbedankt voor het invullen\nsee you at the party.")
