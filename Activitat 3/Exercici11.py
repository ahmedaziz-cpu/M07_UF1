simbols = {
    "Euro": "€",
    "Dolar": "$",
    "Peso": "₡",
    "Rupia": "₹"
}

# Demanar a l'usuari un simbol
simbol = input("Escriu el nom d'una divisa (ex: Euro, Dòlar): ")

#Veure si el simbol està al diccionari i mostrar el símbol
if simbol in simbols:
    print(f"El símbol de {simbol} és: {simbols[simbol]}")
else:
    print("Aquest simbol no està al diccionari.")