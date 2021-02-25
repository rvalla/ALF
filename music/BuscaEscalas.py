Mayor = [0, 2, 4, 5, 7, 9, 11]
Menor = [0, 2, 3, 5, 7, 8, 10]
consost = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]
conbem = ["Dob", "Do", "Reb", "Re", "Mib", "Mi", "Fa", "Solb", "Sol", "Lab", "La", "Sib"]
notain = input("Indica una nota de partida: ")
tipoin = input("Indicá el tipo de escala: ")



def nota_a_numero(nota): #Este está perfecto
    nota_nro = 0
    if nota=="Do":
        nota_nro = 0
        if tipoin == "Menor": #Salvando Do menor
            consost[3] = "Mib"
            consost[8] = "Lab"
            consost[10] = "Sib"
    elif nota=="Dob":
        nota_nro = 0
        conbem[5] = "Fab"
    elif nota=="Sol":
        nota_nro = 7
        if tipoin == "Menor": #Salvando Sol menor
            consost[3] = "Mib"
            consost[10] = "Sib"
    elif nota=="Solb":
        nota_nro = 7
    elif nota == "Re":
        nota_nro = 2
        if tipoin == "Menor":  #Salvando Re menor
            consost[10] = "Sib"
    elif nota=="Reb":
        nota_nro = 2
    elif nota=="La":
        nota_nro = 9
    elif nota=="Lab":
        nota_nro = 9
        if tipoin == "Menor": #Salvando Lab menor
            conbem[5] = "Fab"
    elif nota=="Mi":
        nota_nro = 4
    elif nota=="Mib":
        nota_nro = 4
    elif nota=="Si":
        nota_nro = 11
    elif nota=="Sib":
        nota_nro = 11
    elif nota=="Fa#":
        nota_nro = 6
    elif nota == "Fa":
        nota_nro = 6
    elif nota=="Do#":
        nota_nro = 1
        notas[0] = "Si#"
        notas[5] = "Mi#"

    return nota_nro


def nuevo_patron(numero):
    NvoPatr = []
    for i in tipo:
        i = ((i + numero) % 12)
        NvoPatr.append(i)
    return NvoPatr

def devuelvo_una_escala(patron):
    escala = []
    for i in patron:
       armoescala = notas[i]
       escala.append(armoescala)
    return escala

def imprimo_una_escala(nota, modo):
    if nota == "Fa" or nota == "Sib" or nota == "Mib" or nota == "Lab" or nota == "Reb" or nota == "Solb" or nota == "Dob":
        global notas
        notas = conbem
    else:
        notas = consost

    if modo == "Mayor":
        global tipo
        tipo = Mayor
    elif tipoin == "Menor":
        tipo = Menor

    printscale = devuelvo_una_escala(nuevo_patron(nota_a_numero(notain)))

    print(printscale)


imprimo_una_escala(notain, tipoin)
