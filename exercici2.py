valor_euros = float(input("Valor euros: ")) ##float per que es amb decimals input per fer com un scanner

IVA = int(input("IVA: (4, 10 o 21): "))
while IVA not in (4, 10, 21):  #si no es 4, 10 o 21, torna a demanar el iva
    print("ERROR!")
    IVA = int(input("IVA (4, 10 o 21): ")) 

valor_final = valor_euros + (valor_euros * IVA / 100) # calcula el valor final amb el IVA


print(f"Preu inicial: {valor_euros} euros")
print(f"IVA: {IVA}%")
print(f"Preu final: {valor_final} euros") 

