paraula1 = input("Primera paraula: ")
paraula2 = input("Segona paraula: ")

paraula1, paraula2 = paraula2[:2] + paraula1[2:], paraula1[:2] + paraula2[2:] # canviem les lletres de la segona a la ultima o viceversa

print("La primera paraula es:", paraula1)
print("La segona paraula es:", paraula2)