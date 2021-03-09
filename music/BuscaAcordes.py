#Primero robamos con unos diccionarios, bien a nuestro nuevo estilo. Por terceras propongo por ahora

terceraM = {"Do": "Mi", "Si#": "Rex", "Do#": "Mi#", "Reb": "Fa", "Re": "Fa#", "Re#": "Fax", "Mib": "Sol",
            "Mi": "Sol#", "Fab": "Lab", "Mi#": "Solx", "Fa": "La", "Fa#": "La#", "Solb": "Sib", "Sol": "Si",
            "Sol#": "Si#", "Lab": "Do", "La": "Do#", "La#": "Dox", "Sib": "Re", "Si": "Re#", "Dob": "Mib"}

terceram = {"Do": "Mib", "Si#": "Re#", "Do#": "Mi", "Reb": "Fab", "Re": "Fa", "Re#": "Fa#", "Mib": "Solb",
            "Mi": "Sol", "Fab": "Labb", "Mi#": "Sol#", "Fa": "Lab", "Fa#": "La", "Solb": "Sibb", "Sol": "Sib",
            "Sol#": "Si", "Lab": "Dob", "La": "Do", "La#": "Do#", "Sib": "Reb", "Si": "Re", "Dob": "Mibb"}

inversiones = {"EF": 0, "6": 1, "6/4": 2, "6/5": 1, "4/3": 2, "2": 3}
                #No me acuerdo los cifrados del V9 porque lo enseño en EF!!!!!!!



notain = input("Ingrese una fundamental: ")
modoin = input("Ingrese un tipo de acorde: ")
estado = str(input("Ingrase un estado: "))

acorde = [] #No supe meterlo dentro de las funciones y hacerlo accesible a todas, lo dejo global. No se si entendi bien pero
            #creo que eso me recomendabas hace unas semanas

#Las viejas funciones de hacer subir intervalos
def tercera_M_up(nota):
    tresMup = terceraM[nota]
    acorde.append(tresMup)

def tercera_m_up(nota):
    tresmup = terceram[nota]
    acorde.append(tresmup)

#La fc que arman acordes
def armo_acorde_mayor():
    acorde.append(notain)
    tercera_M_up(notain)
    tercera_m_up(acorde[1])

def armo_acorde_menor():
    acorde.append(notain)
    tercera_m_up(notain)
    tercera_M_up(acorde[1])

def armo_acorde_disminuido():
    acorde.append(notain)
    tercera_m_up(notain)
    tercera_m_up(acorde[1])

def armo_acorde_aumentado():
    acorde.append(notain)
    tercera_M_up(notain)
    tercera_M_up(acorde[1])

def armo_V7():
    armo_acorde_mayor()
    tercera_m_up(acorde[2])

def armo_V9M():
    armo_V7()
    tercera_M_up(acorde[3])

def armo_V9m():
    armo_V7()
    tercera_m_up(acorde[3])

def armo_VII7dim():
    armo_acorde_disminuido()
    tercera_m_up(acorde[2])

def armo_VII7Sen():
    armo_acorde_disminuido()
    tercera_M_up(acorde[2])

tipos = {"Mayor": armo_acorde_mayor, "Menor": armo_acorde_menor, "Disminuido": armo_acorde_disminuido,
         "Aumentado": armo_acorde_aumentado, "V7": armo_V7, "V9M": armo_V9M, "V9m": armo_V9m,
         "VII7Dim": armo_VII7dim, "VII7Sen": armo_VII7Sen} #Para mapear el input

def mapeo_input(modo):#Llama a la fc que corresponde
    tipos[modo]()

def armo_inversion(inv):#Para hacer girar el acorde segun estado
    largo = len(acorde) #Acá si len porque hay acordes de 3 4 o 5 sonidos cargados por ahora
    n = inversiones[inv]
    for i in range(largo): #Agrego la inversion al final de la lista acorde
        o = ((i+n) % largo)
        acorde.append(acorde[o])
    for i in range(largo): #Limpio la lista acorde para que quede solo la inversion sin el EF al ppo
        acorde.pop(0)

def imprimo_acorde(): #Medio al pedo? separé tutti esta vez jajjaj
    print(acorde)

#Esto es para eventualmente combinar con BuscaEscalas y poder imprimir los acordes de una tonalidad
#Ademas porque queria ver que hace esto del "Zip" jaja

escala = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si", "Do"] #La escala que armemos con BuscaEscalas

#Tipos de acorde por grado en una escala determinada (Faltan obvio)
PatronModo = {"Mayor": ["Menor", "Menor", "Mayor", "Mayor", "Menor", "Disminuido", "Mayor", "X"],
              "Menor Antigua": ["Disminuido", "Mayor", "Menor", "Menor", "Mayor", "Mayor", "Menor", "X"]}

def armo_acordes_tonalidad(scale, mode):
    modo = PatronModo[mode]
    global notain
    global modoin
    for (i, j) in zip(scale, modo):
        notain = i
        mapeo_input(modoin) #Aca la cago porque anda pero..... modoin vas a poner menor antigua, porque es tu escala, pero
        print(acorde)       #armo_acorde no funciona con menor antigua, funciona con menor. Lo salve con la vieja cadena de
        acorde.clear()      # menor or menor antigua or menor melodica ....... pero lo borre, prefiero dejarlo incompleto y
        modoin = j          # no que me cagues a pedos jajajajaj
                            #la funcion hace lo suyo pero con estos inputs no


mapeo_input(modoin)
armo_inversion(estado)
imprimo_acorde()
#armo_acordes_tonalidad(escala, modoin)
