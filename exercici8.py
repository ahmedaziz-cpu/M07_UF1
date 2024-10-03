paraules = input("Escriu de 1 a 3 paraules: ").split() #  split() divideix la cadena en una llista de paraules
if len(paraules) < 1 or len(paraules) > 3: # longitud de les paraules maxim 3 paraules minim 1
    print("ERROR!")
else:
    for paraula in paraules:
        print(f"Paraula: {paraula}, Lletres: {len(paraula)}, Primera lletra: {paraula[0]}, Ultima lletra: {paraula[-1]}")