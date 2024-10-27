assignatures = ["Matemàtiques", "Llengua", "Ciències", "Història", "Educació Física", "Anglès"]

# llista buida per emmagatzemar les notes
notes = []

# Demanar a l'usuari que digui les notes
for assignatura in assignatures:
    nota = input(f"Introdueix la nota per a {assignatura}: ")
    notes.append(nota) # ultim valor afegit de la llista

#missatge amb les notes
for i in range(len(assignatures)):
    print(f"A {assignatures[i]} ha tret {notes[i]}.")