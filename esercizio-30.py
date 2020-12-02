numero_cifre=int(input("Salve, qual è il numero di cifre di cui è composto il numero binario che vuole convertire in decimale?"))
print("scriverle una alla volta partendo da destra")
elevatore_potenze=0
numero_decimale=0
for i in range(numero_cifre):
    cifra=int(input())
    numero_somma=cifra*(2**elevatore_potenze)
    numero_decimale+=numero_somma
    elevatore_potenze+=1
numero_binario=input("Se non funziona, provi a riscrivere il numero da sinistra verso destra?")
numero_sicuro=int(numero_binario,2)
if numero_decimale==numero_sicuro:
    print("il numero decimale è ",numero_decimale)
else:
    print("ops")