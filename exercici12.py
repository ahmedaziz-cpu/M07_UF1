numero = int(input("Numero: "))

suma = 0

for x in range(1, numero + 1):
    suma += x  ##afegim el numero actual

print(f"La suma dels numeros des de 1 fins a {numero} es: {suma}")
