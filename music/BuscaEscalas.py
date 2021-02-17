mayor = [0, 2, 4, 5, 7, 9, 11]
notas = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]


nota1 = input("Indica una nota de partida: ")
nota_nro = 0

def quiero_una_escala_con_sost():
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

    for i in mayor:
        escala = ((i + nota_nro) % 12)
        #print(escala, end=" ")
        print(notas[escala])



quiero_una_escala_con_sost()

