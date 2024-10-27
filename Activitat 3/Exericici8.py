# l'usuari intrdueix els 10 numeros
numeros = input("Introdueix 10 números separats per espais: ").split()

# conversio
numeros = [int(num) for num in numeros]

# suma i  mitjana
suma_total = sum(numeros)
mitjana = suma_total / len(numeros)

# suma i la mitjana a la llista
numeros.append(suma_total) # Añade un elemento al final  de la lista

numeros.append(mitjana)  # Añade un elemento al final  de la lista


# Mostrar els resultats
print("Números de l’usuari:", numeros[:-2])  # Mostra lo añadido por el usuario

print("Suma total:", suma_total)
print("Mitjana:", mitjana)