contactes = {}

# demanem contactes
while True:
    nom = input("Escriu un nom: ")

    #  el nom ja existeix
    if nom in contactes:
        print("Ja tens aquest nom. No s'afegeix.")
    else:
        edat = input("Escriu l'edat: ")
        contactes[nom] = edat
        print("Nom afegit.")

    continuar = input("Vols afegir més contactes? (si/no): ")
    if continuar != "si":
        break

#  tots els contactes
print("Els teus contactes són:")
for nom in contactes:
    print(f"{nom} té {contactes[nom]} anys.")