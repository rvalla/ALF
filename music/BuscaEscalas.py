Mayor = [0, 2, 4, 5, 7, 9, 11]
Menor = [0, 2, 3, 5, 7, 8, 11]
notas = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]

notain = input("Indica una nota de partida: ")
tipoin = input("Indicá el tipo de escala: ")

if tipoin == "Mayor": #Bien acá apuntando tipo a la lista patrón
    tipo = Mayor
elif tipoin == "Menor":
    tipo = Menor

def nota_a_numero(nota): #Este está perfecto
    nota_nro = 0
    if nota=="Do":
        nota_nro = 0
    elif nota=="Sol":
        nota_nro = 7
    elif nota == "Re":
        nota_nro = 2
    elif nota=="La":
        nota_nro = 9
    elif nota=="Mi":
        nota_nro = 4
    elif nota=="Si":
        nota_nro = 11
    elif nota=="Fa#":
        nota_nro = 6
        notas[5] = "Mi#"
    elif nota=="Do#":
        nota_nro = 1
        notas[0] = "Si#"

    return nota_nro

def quiero_una_escala(nro_partida, patron):

    for i in patron:
        escala = ((i + nro_partida) % 12)
        print(notas[escala])

#print(quiero_una_escala(nota_a_numero(notain), tipo))
quiero_una_escala(nota_a_numero(notain), tipo)
#Acá estabas imprimiendo un None al final porque print no sabía que imprimir porque la función
#quiero_una_escala no devuelve nada (tiene print adentro)
