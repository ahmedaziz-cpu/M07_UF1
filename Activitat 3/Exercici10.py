
abecedari = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# llistat del abecedari

for i in range(len(abecedari)):
    if (i + 1) % 3 == 0:  # nomes els que no estan a posicio multiple de 3
        abecedari[i] = None  


abecedari = [lletra for lletra in abecedari if lletra is not None]

#imprimeix les lletres que queden
print("Llista resultant tupla y abecedari:", abecedari)
