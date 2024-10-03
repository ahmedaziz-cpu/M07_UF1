import random

numero_secret = random.randint(1, 100) # genera numeros aleatoris entre el rang que li posem

intents = 0

print("Endevina el número entre 1 i 100!")

numero_introduit = 0

while numero_introduit != numero_secret:
    numero_introduit = int(input("Escriu un número: "))
    
    intents += 1
   

    if numero_introduit < numero_secret:
        print("Mes  gran!")
    elif numero_introduit > numero_secret:
        print("Mes  petit!!!")


print(f"Has guanyat en nomes {intents} intents!!!") ## fi del bucle has guanyat
