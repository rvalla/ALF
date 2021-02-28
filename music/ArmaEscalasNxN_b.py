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

#Tetracordios de la menor antigua
def tetrachord_m1():
    p = len(escala) - 1
    tono_up(escala[p])
    stono_up(escala[p+1])
    tono_up(escala[p+2])

#Segundo tetracordios de la menor armónica
def tetrachord_m2():
    p = len(escala) - 1
    tono_up(escala[p])
    stono_up(escala[p+1])
    tono_y_medio_up(escala[p+2])

#Ya tenemos todos los tetracordios
#Vamos a probar otra forma de llamar funciones... ¡Chan!
#Nos hacemos un diccionario que mapea nombres de tetracordios con funciones
tetrachords = {"M1": tetrachord_M1, "M2": tetrachord_M2, "m1": tetrachord_m1, "m2": tetrachord_m2}

#Otro diccionario que guarda qué tetracordios tiene cada escala
escalas = {"Mayor": ["M1", "M2"], "Menor Antigua": ["m1", "m1"], "Menor Armónica": ["m1", "m2"],
			"Menor Melódica": ["m1", "M2"], "Menor Bachiana": ["m1", "M2"]}

#Ojo, esta función sólo va a llamar. Recibe a qué funciones tiene que llamar.
def construir_escala(tetras):
	for t in tetras:
		tetrachords[t]() #Acá estamos llamando a las funciones que corresponden

#Adaptamos la función imprimo_escala para usar la función construir_escala()
def imprimo_escala(modo):
    construir_escala(escalas[modo])
    print(escala)

#¡Ojo! Hice trampa y no resolví las escalas descendentes.

imprimo_escala(modoin)
