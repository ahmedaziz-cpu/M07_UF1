mesos = ["gener", "febrer", "març", "maig", "juny", "agost"]

# Crear una llista buida per emmagatzemar les notes
dies = []

# Demanar a l'usuari que indiqui el mes i dies
for mes in mesos:
    dia = input(f"Introdueix els dies per a {mes}: ")
    dies.append(dia) # ultim valor afegit de la llista

# Mostrar el missatge 
for i in range(len(mesos)):
    print(f"A {mesos[i]} ha tret {dies[i]} dies .")