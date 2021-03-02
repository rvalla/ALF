#Como dije me parece una buena idea. Es una solución elegante. Ahora voy a corregir unas cosas que pasan...

#Muy buena idea esta de guardar los pasos en diccionarios.
tonos = {"Do":"Re", "Do#":"Re#", "Reb":"Mib", "Re":"Mi", "Re#":"Mi#", "Mib":"Fa", "Mi":"Fa#", "Mi#":"Fax",
        "Fab":"Solb", "Fa":"Sol", "Fa#":"Sol#", "Solb":"Lab", "Sol":"La", "Sol#":"La#", "Lab":"Sib", "La":"Si",
        "Sibb":"Dob", "La#":"Si#", "Sib":"Do", "Si":"Do#", "Dob":"Reb"}
stdiat = {"Do":"Reb", "Si#":"Do#", "Do#":"Re", "Re":"Mib", "Re#":"Mi", "Mib":"Fab", "Mi":"Fa", "Mi#":"Fa#",
        "Fab":"Solbb", "Fa":"Solb", "Fa#":"Sol", "Solb":"Labb", "Sol":"Lab", "Sol#":"La", "Lab":"Sibb",
        "La":"Sib", "La#":"Si", "Sib":"Dob", "Si":"Do", "Dob":"Rebb"}
tonymed = {"Do":"Re#", "Do#":"Rex", "Reb":"Mi", "Re":"Mi#", "Re#":"Mix", "Mib":"Fa#", "Mi":"Fa#", "Fab":"Solb",
        "Fa":"Sol#", "Fa#":"Solx", "Solb":"La", "Sol":"La#", "Sol#":"Lax", "Lab":"Si", "La":"Si#", "La#":"Six",
        "Sib":"Do#", "Si":"Do#", "Dob":"Re"}

notain = input("Ingrese una nota: ")
modoin = input("Ingrese un modo: ")

escala = [notain]

def tono_up(note1):
    note2 = tonos[note1]
    escala.append(note2)

def get_tono_up(note1):
    note2 = tonos[note1]
    return note2

def stono_up(notea):
    noteb = stdiat[notea]
    escala.append(noteb)

def get_stono_up(notea):
    noteb = stdiat[notea]
    return noteb

def tono_y_medio_up(nota1):
    nota2 = tonymed[nota1]
    escala.append(nota2)

def get_tono_y_medio_up(nota1):
    nota2 = tonymed[nota1]
    return nota2

#Vamos a probar emprolijar imprimo_escala usando tetracordios (vos dijiste)
#El primer tetracordio de la escala mayor
def tetrachord_M1():
    p = len(escala) - 1  #Siempre empezamos de la última nota de la lista
    tono_up(escala[p])
    tono_up(escala[p+1])
    stono_up(escala[p+2])

#El segundo de la escala mayor
def tetrachord_M2():
    p = len(escala) - 1
    tono_up(escala[p])
    tono_up(escala[p+1])
    tono_up(escala[p+2])
    stono_up(escala[p+3])


#Tetracordios de la menor antigua
def tetrachord_m1():
    p = len(escala) - 1
    tono_up(escala[p])
    stono_up(escala[p+1])
    tono_up(escala[p+2])

#Agregue este tatracordio como segundo de la menor antigua para cerrar en octava
def tetrachord_ma2():
    p = len(escala) - 1
    tono_up(escala[p])
    stono_up(escala[p+1])
    tono_up(escala[p+2])
    tono_up(escala[p + 3])

#Segundo tetracordios de la menor armónica
def tetrachord_m2():
    p = len(escala) - 1
    tono_up(escala[p])
    stono_up(escala[p+1])
    tono_y_medio_up(escala[p+2])
    stono_up(escala[p+3])

#Primer tetracordio modo Dorico
def tatrachord_do1():
    p = len(escala) - 1
    tono_up(escala[p])
    stono_up(escala[p + 1])
    tono_up(escala[p + 2])

#Segundo tetracordio modo Dorico
def tetrachord_do2():
    p = len(escala) - 1
    tono_up(escala[p])
    tono_up(escala[p +1])
    stono_up(escala[p + 2])
    tono_up(escala[p + 3])

#Primer tetracordio modo Frigio
def tetrachord_fr1():
    p = len(escala) - 1
    stono_up(escala[p])
    tono_up(escala[p + 1])
    tono_up(escala[p + 2])

#Primer tetracordio modo Lidio
def tetrachord_li1():
    p = len(escala) - 1
    tono_up(escala[p])
    tono_up(escala[p + 1])
    tono_up(escala[p + 2])

#Segundo tetracordio modo lidio
def tetrachord_li2():
    p = len(escala) - 1
    stono_up(escala[p])
    tono_up(escala[p + 1])
    tono_up(escala[p + 2])
    stono_up(escala[p + 3])

#Ya tenemos todos los tetracordios
#Vamos a probar otra forma de llamar funciones... ¡Chan!
#Nos hacemos un diccionario que mapea nombres de tetracordios con funciones
tetrachords = {"M1": tetrachord_M1, "M2": tetrachord_M2, "m1": tetrachord_m1, "m2": tetrachord_m2,
               "do1": tatrachord_do1, "do2":tetrachord_do2, "ma2": tetrachord_ma2, "fr1": tetrachord_fr1,
               "Li1": tetrachord_li1, "Li2": tetrachord_li2}

#Otro diccionario que guarda qué tetracordios tiene cada escala
escalas = {"Mayor": ["M1", "M2"], "Menor Antigua": ["m1", "m2"], "Menor Armónica": ["m1", "m2"],
			"Menor Melódica": ["m1", "M2"], "Menor Bachiana": ["m1", "M2"], "Dórico": ["do1", "do2"],
           "Frigio": ["fr1", "ma2"], "Lidio": ["Li1", "Li2"], "Mixolidio": ["M1", "do2"]}

#Ojo, esta función sólo va a llamar. Recibe a qué funciones tiene que llamar.
def construir_escala(tetras):
	for t in tetras:
		tetrachords[t]() #Acá estamos llamando a las funciones que corresponden

#¡Bajé la función imprimo_escala!

#¡Ojo! Hice trampa y no resolví las escalas descendentes.

#Aca abajo una idea que surgio a partir de pensar en los modos griegos.
#Pensaba que no necesitamos escribir mas tatracordios porque podemos escribir los modos como una escala mayor
#transportada. por ejemplo Re dorico es la escala de Do Mayor leida desde el Re y asi con todos los modos
#Por ejemplo para Sol.  Dorico(escala mayor tono abajo. Fa)
#                       frigio(idem tercera mayor abajo. Mib)
#                       Lidio(idem, cuarta j abajo. Re)
#                       mixolidio(idem 5j. Do)
#El problema es hacer mover el input ese intervalo hacia abajo, no se me ocurrió un modo de hacerlo sin ensuciar esto
#que está bastante prolijo. pero dejo esta función que puede dispararte alguna idea incluso nos puede servir para otra cosa.
#Obviamente si no disparas imprimo_escala antes no hace nada y si lo corres habiendo pedido un modo antes va a tirar fruta
# yyyyyyyy....... Ya se que es lagra y que hace mas de una cosa, yo escribo para abajo y despues veo!!! jajaa

#Esto es lo que yo hubiera hecho. Aunque seguís desaprovechando el hecho de que las funciones pueden recibir parámetros.
#Acá está la tuya
def get_scale_modes():
    largo = len(escala) #Esto sobra porque la función sólo funciona si recibe listas de 7...
    dorico = []
    frigio = []
    lidio = []
    mixolidio = []
    for i in range(largo):
        transp = (i+1)%7 #¡Porque acá está el 7!
        dorico.append(escala[transp])
    print("Dorico: ", dorico)
    for i in range(largo):
        transp = (i+2)%7
        frigio.append(escala[transp])
    print("Frigio: ", frigio)
    for i in range(largo):
        transp = (i+3)%7
        lidio.append(escala[transp])
    print("Lidio: ", lidio)
    for i in range(largo):
        transp = (i+4)%7
        mixolidio.append(escala[transp])
    print("Mixolidio: ", mixolidio)

#A mí me gusta escribir menos.
#Primero robamos con otro diccionario
gregorian_modes = {"Dórico": 1, "Frigio": 2, "Lidio": 3, "Mixolidio": 4}

#Para no hacer lío le paso a la funciónn también la escala
def get_scale_modes_clean(gregorian_mode, scale):
	notes = []
	g = gregorian_modes[gregorian_mode]
	for i in range(7):
		notes.append(scale[(i+g)%7])
	notes.append(notes[0])
	return notes

#Adaptamos la función imprimo_escala para usar la función construir_escala() y aceptar modos gregorianos
def imprimo_escala(modo):
	if modoin in ["Mayor", "Menor Antigua", "Menor Armónica", "Menor Melódica", "Menor Bachiana"]:
		construir_escala(escalas[modo])
		print(notain, end=" ")
		print(modo, end=": ")
		print(escala, end="\n")
	else:
		construir_escala(escalas["Mayor"])
		print(notain, end=" ")
		print(modo, end=": ")
		print(get_scale_modes_clean(modo, escala), end="\n")

imprimo_escala(modoin)
#get_scale_modes()
