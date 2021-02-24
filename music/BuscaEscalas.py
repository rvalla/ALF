Mayor = [0, 2, 4, 5, 7, 9, 11]
Menor = [0, 2, 3, 5, 7, 8, 10]
#notas = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]
#notas2 = ["Dob", "Do", "Reb", "Re", "Mib", "Mi", "Fa", "Solb", "Sol", "Lab", "La", "Sib"]
consost = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]
conbem = ["Dob", "Do", "Reb", "Re", "Mib", "Mi", "Fa", "Solb", "Sol", "Lab", "La", "Sib"]
notain = input("Indica una nota de partida: ")
tipoin = input("Indicá el tipo de escala: ")

if tipoin == "Mayor": #Bien acá apuntando tipo a la lista patrón
    tipo = Mayor
elif tipoin == "Menor":
    tipo = Menor

"""Este no funciona"""
#if notain == ["Fa", "Sib", "Mib", "Lab", "Reb", "Solb", "Dob"]:
#    notas = conbem
#else:
#    notas = consost


"""este funciona"""
if notain == "Fa" or notain == "Sib" or notain == "Mib" or notain == "Lab" or notain == "Reb" or notain == "Solb" or notain == "Dob":
    notas = conbem
else:
    notas = consost

"""Este funciona pero hay que activar lineas 3 y 4"""
#if notain == "Fa":
 #   notas = notas2
#elif notain == "Sib":
 #   notas = notas2
#elif notain == "Mib":
 #   notas = notas2
#elif notain == "Lab":
 #   notas = notas2
#elif notain == "Reb":
  #  notas = notas2
#elif notain == "Solb":
   # notas = notas2
#elif notain == "Dob":
    #notas = notas2





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
    elif nota=="La": #Be careful here. Pasan cosas... Zafo!!
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
