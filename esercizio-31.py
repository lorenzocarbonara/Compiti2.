numero_decimale=int(input("inserire il numero decimale che vuole trasformare in binario"))
bin(numero_decimale) #bin converte un numero decimale in un numero binario#
numeri_binari=[]
numeri_binari.append(numero_decimale%2)
while numero_decimale!=1:
    numero_decimale//=2
    resto=numero_decimale%2
    numeri_binari.append(resto)
numeri_binari.reverse()
print("Il numero trasformato in binario è:")
for number in numeri_binari:
    print(number,end="")
print("fine")