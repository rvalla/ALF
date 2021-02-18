<<<<<<< HEAD
Mayor = [0, 2, 4, 5, 7, 9, 11]
Menor = [0, 2, 3, 5, 7, 8, 11]
=======
mayor = [0, 2, 4, 5, 7, 9, 11] #Excelente
>>>>>>> 15c36100b4a8388645258a217d887bdea9ef956c
notas = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]

notain = input("Indica una nota de partida: ")
tipoin = input("Indicá el tipo de escala: ")

<<<<<<< HEAD
if tipoin == "Mayor":
    tipo = Mayor
elif tipoin == "Menor":
    tipo = Menor

def nota_a_numero(nota):
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
=======
nota1 = input("Indica una nota de partida: ")
nota_nro = 0 #Así como está podés definir esta variable adentro de la función (afuera nadie la necesita)

def quiero_una_escala_con_sost():
	#Esta función se puede subdividir
	#Esta cadena de if, elif... debería ser una función como "nota_a_numero(nota)"
	#que reciba un nombre y devuelva un número (porque la vas a usar con
	#"quiero_una_escala_menor_bachiana()"
	#"quiero_una_escala_x" tiene entonces que recibir un número (nota_nro)
	if nota1=="Do":
		nota_nro = 0
	elif nota1=="Sol":
		nota_nro = 7
	elif nota1 == "Re":
		nota_nro = 2
	elif nota1=="La":
		nota_nro = 9
	elif nota1=="Mi":
		nota_nro = 4
	elif nota1=="Si":
		nota_nro = 11
	elif nota1=="Fa#":
		nota_nro = 6
		notas[5] = "Mi#"
	elif nota1=="Do#":
		nota_nro = 1
		notas[0] = "Si#"

	for i in mayor: #Esta es tu función
		#De hecho podrías tener este bucle en una función que reciba una nota de partida y el patrón,
		#Porque para todas las escalas va a ser igual...
		escala = ((i + nota_nro) % 12)
		#print(escala, end=" ")
		print(notas[escala])
>>>>>>> 15c36100b4a8388645258a217d887bdea9ef956c

def quiero_una_escala(nro_partida, patron):

    for i in patron:
        escala = ((i + nro_partida) % 12)
        print(notas[escala])

print(quiero_una_escala(nota_a_numero(notain), tipo))

#Creo que de tarea quedaría:
# -Sacar el if elif para hacer la función nota_a_numero
# -Hacer una función general que reciba nota de partida y patrón y fabrique la escala
# -Hacer la función que llama a esa función general
