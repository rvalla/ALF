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

#Para la escala hexafonica sumar dos tetacordios lidios y sacar el ultimo sonido
def hexafonica():
    escala.pop(6)

#Para los modos pentatonicos propongo armar escalas mayores o menores antiguas y remover notas de esas escalas.
#El unico metodo que conozco es el "Pop" y no me deja poner dos posiciones, me lleva dos lineas
def penta_modo_1():
    escala.pop(3) #Muy bien acá. I like it.
    escala.pop(5)

def penta_modo_2():
    escala.pop(1)
    escala.pop(4)

def penta_modo_3():
    escala.pop(2)
    escala.pop(5)

def penta_modo_4():
    escala.pop(1)
    escala.pop(3)

def penta_modo_5():
    escala.pop(2)
    escala.pop(4)

#Ya tenemos todos los tetracordios
#Vamos a probar otra forma de llamar funciones... ¡Chan!
#Nos hacemos un diccionario que mapea nombres de tetracordios con funciones
tetrachords = {"M1": tetrachord_M1, "M2": tetrachord_M2, "m1": tetrachord_m1, "m2": tetrachord_m2,
               "do1": tatrachord_do1, "do2":tetrachord_do2, "ma2": tetrachord_ma2, "fr1": tetrachord_fr1,
               "Li1": tetrachord_li1, "Li2": tetrachord_li2, "Pent": penta_modo_1, "Pent2": penta_modo_2,
               "Pent3": penta_modo_3, "Pent4": penta_modo_4, "Pent5": penta_modo_5, "Hex": hexafonica}

#Otro diccionario que guarda qué tetracordios tiene cada escala
escalas = {"Mayor": ["M1", "M2"], "Menor Antigua": ["m1", "ma2"], "Menor Armónica": ["m1", "m2"],
			"Menor Melódica": ["m1", "M2"], "Menor Bachiana": ["m1", "M2"], "Dórico": ["do1", "do2"],
           "Frigio": ["fr1", "ma2"], "Lidio": ["Li1", "Li2"], "Mixolidio": ["M1", "do2"],
           "Pentatonico modo 1": ["M1", "M2", "Pent"], "Pentatonico modo 2": ["m1", "ma2", "Pent2"],
           "Pentatonico modo 3": ["M1", "M2", "Pent3"], "Pentatonico modo 4": ["m1", "ma2", "Pent4"],
           "Pentatonico modo 5": ["m1", "ma2", "Pent5"], "Hexafonica": ["Li1", "Li1", "Hex"]}

#Ojo, esta función sólo va a llamar. Recibe a qué funciones tiene que llamar.
def construir_escala(tetras):
	for t in tetras:
		tetrachords[t]() #Acá estamos llamando a las funciones que corresponden

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
def get_scale_modes():
    largo = len(escala) #Esto está de más, sólo anda con 7
    dorico = []
    frigio = []
    lidio = []
    mixolidio = []
    for i in range(7):#range(largo):
        transp = (i+1)%7 #¡Porque el 7 ya está acá!
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

#Vamos a poner un poco de orden
#Tenemos una serie de modos que construimos
default_modes = ["Mayor", "Menor Antigua", "Menor Armónica", "Menor Melódica", "Menor Bachiana",
				"Pentatonico modo 1", "Pentatonico modo 2", "Pentatonico modo 3", "Pentatonico modo 4",
	            "Pentatonico modo 5", "Hexafonica"]
#Vamos a hacer trampa para los modos gregorianos partiendo del modo Mayor...

#Adaptamos la función imprimo_escala para usar la función construir_escala() y aceptar modos gregorianos
def imprimo_escala(modo):
	if modoin in default_modes:
		construir_escala(escalas[modo])
		print(notain, end=" ")
		print(modo, end=": ")
		print(escala, end="\n")
	else:
		construir_escala(escalas["Mayor"])
		print(notain, end=" ")
		print(modo, end=": ")
		print(get_scale_modes_clean(modo, escala), end="\n") #De la manera que usas esta función estas recibiendo el modo
                                                             #gregoriano "X" con las notas de la tonalidad que pediste.
                                                             #La idea basica de BuscaEscalas es que pongas la tonica y te de la
                                                             #escala. Asi, si pones Do Dorico te da re, mi, fa, sol etc y no
                                                             #Do, Re, Mib, Fa etc. Mi idea sobre la función get_scale_modes era que una vez
                                                             #que tenias tus escala la hacias girar y te daba los modos posibles. Un resabio de
                                                             #Un intento original que deje ahi por si servía de algo. la correccion de la funcion esta
                                                             #genal de todos modos

imprimo_escala(modoin)
#get_scale_modes()  #No correr con modos pentatonicos ni menores!!! Explotará!!! Idem Hexafonica!
