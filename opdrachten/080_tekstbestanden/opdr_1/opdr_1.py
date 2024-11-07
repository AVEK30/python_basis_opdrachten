inputuser = input("wat vind u van het huidige kabinet \n")
with open ("input.txt", "w") as file:
    file.write(inputuser + "\n")


inputuser = input("Wat vind je van de Python-lessen tot nu toe? \n")
with open ("input.txt", "a") as file:
    file.write(inputuser + "\n")
 
inputuser = input("Wat vind jij de mooiste stad van Nederland? \n")
with open ("input.txt", "a") as file:
    file.write(inputuser + "\n")


