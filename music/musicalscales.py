#Desafío: Hacer un programa que pueda escribir correctamente las escalas musicales de todas las tonalidades.

#Vamos a dividir el problema de las escalas musicales en dos partes:
#1. Construir el subconjunto de notas que conforma la escala.
#2. Escribirla correctamente distinguiendo henarmonías.

#Representación de las notas
#Vamos a representar las clases de alturas usando el conjunto Z_12 (los restos de dividir por 12).
#Por convención 0 = Do ... 11 = Si
note_classes = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "Sib", "Si"]

#Necesitamos traducir la escala pedida (por ejemplo: Dob mayor). Vamos a usar diccionarios:
scale_names_dict = {
	"Dob": 11, "Do": 0, "Do#": 1, "Reb": 1, "Re": 2, "Re#": 3,
	"Mib": 3, "Mi": 4, "Mi#": 5, "Fab": 4, "Fa": 5, "Fa#": 6,
	"Solb": 6, "Sol": 7, "Sol#": 8,	"Lab": 8, "La": 9, "La#": 10,
	"Sib": 10, "Si": 11, "Si#": 0
}
#Una vez conocida la nota de partida sólo hay que trasladar el patrón (sumar)
scale_patterns_up = {
	"major": [0,2,4,5,7,9,11],
	"antique": [0,2,3,5,7,8,10],
	"harmonic": [0,2,3,5,7,9,10],
	"melodic": [0,2,3,5,7,9,11],
}
scale_patterns_down = {
	"major": [0,11,9,7,5,4,2],
	"antique": [0,10,8,7,5,3,2],
	"harmonic": [0,10,9,7,5,3,2],
	"melodic": [0,10,8,7,5,3,2],
}

#Necesitamos una manera de distinguir henarmonías (por ejemplo entre Lab y Sol#)
#Vamos a dividir el trabajo en dos partes:
#1. Nombre de la altura (Do, re, mi...)
#2. Alteración accidental (b, #...)
note_names = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"]
note_names_dict = {
	"Dob": 0, "Do": 0, "Do#": 0, "Reb": 1, "Re": 1, "Re#": 1,
	"Mib": 2, "Mi": 2, "Mi#": 2, "Fab": 3, "Fa": 3, "Fa#": 3,
	"Solb": 4, "Sol": 4, "Sol#": 4,	"Lab": 5, "La": 5, "La#": 5,
	"Sib": 6, "Si": 6, "Si#": 6
}
#Para decidir qué alteración corresponde vamos a mirar la distancia de la nota con respecto a su valor becuadro
note_centers = [0,2,4,5,7,9,11]
note_offsets = ["", "#", "##", "###", "*", "*", "*", "*", "*", "bbb", "bb", "b"]

#Para empezar necesitamos traducir la tonalidad solicitada guardandonos el nombre de partida y el valor de la altura
def translate_note(name):
	try:
		return scale_names_dict[name], note_names_dict[name]
	except:
		print("I couldn't translate that note!", end="\n")

#Esta función sólo traduce una lista de notas a números, pero no se fija en el nombre (es para otra cosa)
def translate_list(note_list):
	new_list = []
	for i in range(len(note_list)):
		new_list.append(translate_note(note_list[i]))
	return new_list

#Acá tenemos las funciones que pensamos llamar para construir una escala o una lista de notas
#Para imprimir una escala ascendente
def print_scale_up(note, type):
	#Primero construimos la escala
	scale_data = build_scale(note, type, 1)
	#Después la escribimos correctamente
	return print_notes(scale_data[0], scale_data[1], 1)

#Para imprimir una escala descendente
def print_scale_down(note, type):
	scale_data = build_scale(note, type, -1)
	return print_notes(scale_data[0], scale_data[1], -1)

#Capaz queremos imprimir una escala que sube y baja (ya que estamos...)
def print_scale_up_and_down(note, type):
	scale_text = ""
	scale_data = build_scale(note, type, 1)
	scale_text += print_notes(scale_data[0], scale_data[1], 1)
	scale_data = build_scale(note, type, -1)
	scale_text += print_notes(scale_data[0], scale_data[1], -1)
	return scale_text

#A veces quizás sólo querés trasponer una lista de notas (esta es para eso)
def print_transpose_notes(list, distance):
	note_list = translate_list(list)
	print_notes(transpose_notes(note_list, distance))

#A function to tranpose notes
def transpose_notes(note_list, distance):
	new_list = []
	for i in range(len(note_list)):
		new_list.append(note_list[i] + distance)
	return new_list

#Esta es la función que construye la escala musical
def build_scale(note, type, direction):
	#Primero traduce la nota pedida
	note_class, note_value = translate_note(note)
	#Decide qué patrón usar
	if direction == 1:
		pattern = scale_patterns_up[type]
	elif direction == -1:
		pattern = scale_patterns_down[type]
	else:
		#Siempre podemos llamar mal una función
		print("Scale direction is wrong...", end ="\n")
	#La función devuelve la posición del nombre a la nota en note_names y la lista de alturas
	return note_value, transpose_notes(pattern, note_class)

#¡Estamos a punto de ver la función estrella, la que transforma una lista de números en las caprichosas
#formas de nombrar alturas usadas por Bach, Mozar, Beethoven y vos.
#Antes de seguir quizás es importante tener en cuenta que el resto una división es siempre positivo. En Z
#(el conjunto de los números enteros) -1 / 5 = -1*5 + 4 (el resto no es -1, es 4). Así que si en el código
#del programa dice -1%5 es 4. ¡Chan!

#Vamos a hacer lo siguiente:
#1. Vamos a tener que recorrer las 7 notas de la escala definiendo nombre y alteración accidental (bucle)
#	1.1. Calculamos la posición del nombre de la nota en note_names que es:
#			número de iteración * dirección + posición de partida % 7
#			Como los restos son > 0 podemos recorrer la lista marcha atrás. ¡Chan!
#	1.2. Calculamos la distancia entre la nota de nuestra escala y la nota becuadro
#			Como la función transpose_notes no se preocupa por mantener los valores < 12 (no se fija en
#			los cambios de octava) nos quedamos con la distancia % 12. Nuestra distancia es la posición
#			de la alteración en note_offsets.
#	1.3. Agregamos la alteración
#¿Por qué note_offsets es una lista de 12 cosas? Sí sobran. Pero es una manera sencilla de que no se arme
#lío con las distancias. En Z_12 11 = -1. Pero eso no es lo mismo en otros conjuntos. Por ejemplo podemos
#usar Z_5 ("", "#", "##", "bb", "b") pero en ese conjunto 11 = 1. Da problemas con Dob o Si#.

#¡Aquí está la función del poder! Ya nada puede detenernos...
#Recibe la nota de partida, la lista con los valores de la escala, d en {-1,1} para decidir dirección.
def print_notes(note_class, note_l, direction):
	#Vamos a guardar la escala en una cadena de texto
	scale_text = "The notes are: "
	for i in range(7):
		#Empezamos a construir la nueva nota
		new_note = ""
		#Calcularmos en qué posición está el nombre de la nota en note_names
		p = ((i * direction) + note_class) % 7
		new_note += note_names[p] #Nos guardamos el nombre
		#Calculamos a qué distancia está nuestra nota de la nota becuadro
		o = (note_l[i] - note_centers[p]) % 12
		new_note += note_offsets[o] #Agregamos la alteración
		#Seamos prolijos, no poonemos coma al final
		if i < 6:
			new_note += ", "
		#Agregamos la nueva nota a la cadena
		scale_text += new_note
	return scale_text

#Es posible que no te preocupen las henarmonías. En ese caso esta función es para vos.
def print_notes_12(note_list):
	scale_text = "The notes are: "
	for i in range(len(note_list)):
		scale_text += note_classes[note_list[i]%12] + " "
	print(scale_text, end="\n")
