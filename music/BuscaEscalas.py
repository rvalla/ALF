mayor = [0, 2, 4, 5, 7, 9, 11] #Excelente
notas = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]


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



quiero_una_escala_con_sost()

#Creo que de tarea quedaría:
# -Sacar el if elif para hacer la función nota_a_numero
# -Hacer una función general que reciba nota de partida y patrón y fabrique la escala
# -Hacer la función que llama a esa función general
