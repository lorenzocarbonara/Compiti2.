escursioni_città=[]
escursione_gradi=[]
valore_di_controllo=float(input("quanti gradi vale il valore prefissato per il controllo dell'escursione termica che si desidera monitorare?"))
print("Per fermare il programma digitare 0")
while True:
    nome=input("Nome della città")
    if nome=="0":
        break
    print("Gradi della temperatura massima registrata a ",nome,"?")
    temperatura_massima=float(input())
    print("Gradi della temperatura minima registrata a ",nome,"?")
    temperatura_minima=float(input())
    escursione=temperatura_massima-temperatura_minima
    if escursione>=valore_di_controllo:
        escursioni_città.append(nome)
        escursione_gradi.append(escursione)
print("hanno superato il valore prefissato le seguenti ",len(escursioni_città)," città:")
index_città=0
for i in range(len(escursioni_città)):
    print(escursioni_città[index_città]," con un'escursione di", escursione_gradi[index_città]," gradi")
    index_città+=1