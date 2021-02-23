Mayor = [0, 2, 4, 5, 7, 9, 11]
Menor = [0, 2, 3, 5, 7, 8, 10]
notas = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]
notas2 = ["Dob", "Do", "Reb", "Re", "Mib", "Mi", "Fa", "Solb", "Sol", "Lab", "La", "Sib"]
notain = input("Indica una nota de partida: ")
tipoin = input("Indicá el tipo de escala: ")

if tipoin == "Mayor": #Bien acá apuntando tipo a la lista patrón
    tipo = Mayor
elif tipoin == "Menor":
    tipo = Menor

if notain == "Fa" or "Sib" or "Mib" or "Lab" or "Reb" or "Solb" or "Dob" or "Fab":
    notas = notas2 #Ok, no está mal. Resuelve.


def nota_a_numero(nota): #Este está perfecto
    nota_nro = 0
    if nota=="Do":
        nota_nro = 0
    elif nota=="Dob":
        nota_nro = 0
    elif nota=="Sol":
        nota_nro = 7
    elif nota=="Solb":
        nota_nro = 7
    elif nota == "Re":
        nota_nro = 2
    elif nota=="Reb":
        nota_nro = 2
    elif nota=="La": #Be careful here. Pasan cosas...
        nota_nro = 9
    elif nota=="Lab":
        nota_nro = 9
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

print(devuelvo_una_escala(nuevo_patron(nota_a_numero(notain))))
