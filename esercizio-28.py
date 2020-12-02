nomi_studenti=[]
valori=[]
print("Per interrompere la lista, digitare 0 ")
while True:  
    nome=input("Inserire nome studente ")
    if nome =="0": 
        break
    lancio=float(input("inserire il valore del lancio in metri "))
    nomi_studenti.append(nome)
    valori.append(lancio)
indice_vincitore=valori.index(max(valori))
valore_vincitore=max(valori)
vincitore=nomi_studenti[indice_vincitore]
print("ha vinto", vincitore, "con un lancio di", valore_vincitore, "metri.")