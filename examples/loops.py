list = [0,2,4,6,8,10]
list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list3 = [0, 4, 8, 12, 16, 20, 24, 28, 32]
list4 = [0, 3, 6, 9, 12, 15, 18]

try:
	print("- for i in list:", end="\n")
	for i in list:
		print(i, end=" ")
		print(list[i], end="\n")
		print("", end="\n") #Esta linea no entiendo que está haciendo. #No se si toque algo sin querer
							#pero al escribir mas abajo si que cambia la distrubucion del texto.
except:
	print("Houston, we have a problem!", end="\n")
	print("", end="\n")

print("AAAAAAAAAAAAAAAAAAAAAA")

for i in list2: #un intento de entender que hace list[i]
	print(list2[i], end=" ") #ehh? me devuelve lo mismo que print[i] y no tira error
	print(i, end="\n") #por si estoy loco
	#ok, devuelve lo mismo que print[i], será por ser de numeros consecutivos?

print("BBBBBBBBBBBBBBBBBBBBBBB")

try:
	for i in list3: #segndo intento
		print(list3[i]) #ahora se cae, fuera de rango, pongo excepción # una cagada lo que devuelve, el 1 y el 16
						#por ahi como va de 4 en 4 tira el primer valor y salta 4, despues queda fuera de rango.
						#pruebo alargando la lista. #devuelve lo esperado, sera?
except:
	print("XXX")

print("CCCCCCCCCCCCCCCCCCCCCCCCCC")

try:
	for i in list4:
		print(list4[i]) #Deberia darme 0, 9, 18 #Lo hace, aunque siempre la explicacion puede ser otra jajaja
												#Lo importante es que tu teoría te permita hacer predicciones jajaj
except:
	print("XXX")

#Esclarecido por Rodrigo via wapp. list[i] devuelve el elemento en la posicion i, lo que sea que valga i en esa vuelta claro
#Aquello de que no cuenta el primer elemento es la vieja huevada de empezar a contar por el cero.
#Despues no se quejen de los que hablan con la N o deciden casarse con su heladera, hagan lo que quieran.

print("AQUI DEJAMOS DE JUGAR CON LIST[I]")


try:
	print("- for i in range(len(list)):", end="\n")
	for i in range(len(list)):
		print(i, end=" ")
		print(list[i], end="\n")
	print("", end="\n")
except:
	print("Houston, we have a problem!", end="\n")
	print("", end="\n")

try:
	print("- for i in enumerate(list):", end="\n")
	for i, n in enumerate(list):
		print(n, end=" ")
		print(list[i], end="\n")
	print("", end="\n")
except:
	print("Houston, we have a problem!", end="\n")
	print("", end="\n")
