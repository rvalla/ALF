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

#Estas funciones están bien pero... Estás haciendo el trabajo dos veces.
#Está bien note2 = tonos[note1] pero después tendrías que elegir entre
#que la función agregue la nota a la lista o retorne la nota a agragar.
#Acá agregás (vos la estás llamando en imprimo_escala pensandola así)
def tono_up(note1):
    note2 = tonos[note1]
    escala.append(note2)

#Acá devolvés la nueva nota. Tendrías que llamarla escala.append(get_tono_up(note1))
def get_tono_up(note1):
    note2 = tonos[note1]
    return note2

#Vale lo mismo para estas
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

#Adaptamos la función imprimo_escala para usar las funciones tetrachord_xx
def imprimo_escala(modo):
    if modo == "Mayor":
        tetrachord_M1()
        tetrachord_M2()
        print(escala)
    elif modo == "Menor Antigua":
        tetrachord_m1()
        tetrachord_m1()
        print(escala)
    elif modo == "Menor Armónica":
        tetrachord_m1()
        tetrachord_m2()
        print(escala)
    elif modo == "Menor Melódica":
        tetrachord_m1()
        tetrachord_M2()
        print(escala)
        escala.clear()
        escala.append(notain)
        tetrachord_m1()
        tetrachord_m1()
        print(escala[::-1])
    elif modo == "Menor Bachiana":
        tetrachord_m1()
        tetrachord_M2()
        print(escala)
        escala.clear()
        escala.append(notain)
        tetrachord_m1()
        tetrachord_M2()
        print(escala[::-1])

imprimo_escala(modoin)
