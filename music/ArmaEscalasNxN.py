tonos = {"Do":"Re", "Do#":"Re#", "Reb":"Mib",
         "Re":"Mi", "Re#":"Mi#", "Mib":"Fa",
         "Mi":"Fa#", "Mi#":"Fax", "Fab":"Solb",
         "Fa":"Sol", "Fa#":"Sol#", "Solb":"Lab",
         "Sol":"La", "Sol#":"La#", "Lab":"Sib",
         "La":"Si", "Sibb":"Dob", "La#":"Si#",
         "Sib":"Do", "Si":"Do#", "Dob":"Reb"}
stdiat = {"Do":"Reb", "Si#":"Do#", "Do#":"Re", "Re":"Mib",
          "Re#":"Mi", "Mib":"Fab", "Mi":"Fa", "Mi#":"Fa#", "Fab":"Solbb",
          "Fa":"Solb", "Fa#":"Sol", "Solb":"Labb", "Sol":"Lab",
          "Sol#":"La", "Lab":"Sibb", "La":"Sib", "La#":"Si", "Sib":"Dob",
          "Si":"Do", "Dob":"Rebb"}
tonymed = {"Do":"Re#", "Do#":"Rex", "Reb":"Mi", "Re":"Mi#", "Re#":"Mix", "Mib":"Fa#",
           "Mi":"Fa#", "Fab":"Solb", "Fa":"Sol#", "Fa#":"Solx", "Solb":"La", "Sol":"La#",
           "Sol#":"Lax", "Lab":"Si", "La":"Si#", "La#":"Six", "Sib":"Do#", "Si":"Do#", "Dob":"Re"}

notain = input("Ingrese una nota: ")
modoin = input("Ingrese un modo: ")

escala = [notain,]

def tono_up(note1):
    note2 = tonos[note1]
    escala.append(note2)
    return note2

def stono_up(notea):
    noteb = stdiat[notea]
    escala.append(noteb)
    return noteb

def tono_y_medio_up(nota1):
    nota2 = tonymed[nota1]
    escala.append(nota2)
    return nota2

def imprimo_escala(modo):
    if modo == "Mayor":
        tono_up(notain)
        tono_up(escala[1])
        stono_up(escala[2])
        tono_up(escala[3])
        tono_up(escala[4])
        tono_up(escala[5])
        stono_up(escala[6])
        print(escala)
    elif modo == "Menor Antigua":
        tono_up(notain)
        stono_up(escala[1])
        tono_up(escala[2])
        tono_up(escala[3])
        stono_up(escala[4])
        tono_up(escala[5])
        tono_up(escala[6])
        print(escala)
    elif modo == "Menor Armónica":
        tono_up(notain)
        stono_up(escala[1])
        tono_up(escala[2])
        tono_up(escala[3])
        stono_up(escala[4])
        tono_y_medio_up(escala[5])
        stono_up(escala[6])
        print(escala)
    elif modo == "Menor Melódica":
        tono_up(notain)
        stono_up(escala[1])
        tono_up(escala[2])
        tono_up(escala[3])
        tono_up(escala[4])
        tono_up(escala[5])
        stono_up(escala[6])
        print(escala)
        escala.clear()
        escala.append(notain)
        tono_up(notain)
        stono_up(escala[1])
        tono_up(escala[2])
        tono_up(escala[3])
        stono_up(escala[4])
        tono_up(escala[5])
        tono_up(escala[6])
        print(escala[::-1])
    elif modo == "Menor Bachiana":
        tono_up(notain)
        stono_up(escala[1])
        tono_up(escala[2])
        tono_up(escala[3])
        tono_up(escala[4])
        tono_up(escala[5])
        stono_up(escala[6])
        print(escala)
        print(escala[::-1])




imprimo_escala(modoin)
