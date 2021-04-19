import random

techo = "+ ------- +"
dos = "|  x   x  |"
izq = "|  x      |"
der = "|      x  |"
ctro = "|    x    |"
nada = "|         |"
vacio = ""


def draw_dice(n): #Esto no lo uso, primera prueba para dibujar un dado
    if n == 1:
        print(techo + "\n" + nada + "\n" + ctro + "\n" + nada + "\n" + techo)
    elif n == 2:
        print(techo + "\n" + der + "\n" + nada + "\n" + izq + "\n" + techo)
    elif n == 3:
        print(techo + "\n" + der + "\n" + ctro + "\n" + izq + "\n" + techo)
    elif n == 4:
        print(techo + "\n" + dos + "\n" + nada + "\n" + dos + "\n" + techo)
    elif n == 5:
        print(techo + "\n" + dos + "\n" + ctro + "\n" + dos + "\n" + techo)
    elif n == 6:
        print(techo + "\n" + dos + "\n" + dos + "\n" + dos + "\n" + techo)


#Un diccionario!!!!! lo uso para dibujar varios dados en linea
dicedraw = {0: [vacio, vacio, vacio, vacio, vacio], 1: [techo, nada, ctro, nada, techo], 2: [techo, der, nada, izq, techo],
            3: [techo, der, ctro, izq, techo], 4: [techo, dos, nada, dos, techo],
            5: [techo, dos, ctro, dos, techo], 6: [techo, dos, dos, dos, techo]}

counter = 0
repeated = []
numbers = []

def draw_dices(n): #Dibuja en linea
    for i, j, k, l, m in zip(dicedraw[n[0]], dicedraw[n[1]], dicedraw[n[2]],
                             dicedraw[n[3]], dicedraw[n[4]]):
        print(i, " ",  j, " ", k, " ", l, " ", m)

def roll_dice(n): #Tira
    for i in range(n):
        a = random.randint(1, 6)
        numbers.append(a)

def find_repeated(): #Manera muy cabeza de detectar pares de numeros
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    for i in numbers:
        if i == 1:
            one += 1
        elif i == 2:
            two += 1
        elif i == 3:
            three += 1
        elif i == 4:
            four += 1
        elif i == 5:
            five += 1
        elif i == 6:
            six += 1
    loop = [one, two, three, four, five, six]
    for i in loop:
        repeated.append(i)
    return repeated

def is_game(r): #Manera muy cabeza de ver si hay algun juego. Escalera olvidate, no se me ocurrio. por ahi con tu is_fibo?
    havetwo = False  #pero al poner el seis al final se caga. veremos, hay tres combinaciones, si me apuras las escribo todas
    havethree = False
    havefour = False
    havefive = False
    havenone = False
    c = 0
    for i in r:
        if i == 2:
            havetwo = True
        elif i == 3:
            havethree =True
        elif i == 4:
            havefour = True
        elif i == 5:
            havefive = True
        elif i == 1:
            c += 1
    if c == 5:
        havenone = True
    if havetwo and havethree:
        return "Full"
    elif havefour:
        return "Poker"
    elif havefive:
        return "Generala"
    elif havenone:
        if sum(numbers) == 15 or sum(numbers) == 19 or ssum(numbers) == 20:
            return "Escalera"
    else:
        return "No game"

def pick_dice(): #Para elegir cuales te quedas
    conuter = 0
    descarte = True
    if input("Descartas dados? s/n: ") == "n": #Te pregunta la ubicacion del dado no el numero que sacas. Puede confundir
        descarte = False
    while descarte:
        conuter += 1
        numbers.pop(int(input("Que dado mandas al cubilete?: ")) - 1)
        numbers.append(0)
        print("Tus dados son: ")
        draw_dices(numbers)
        if input("Descartas mas dados? s/n: ") == "n":
            descarte = False
    for i in range(conuter):
        numbers.pop()





# Esto es una garompa a modo de prueba de un posible algoritmo de juego con lo poco que hace esto por ahora
while counter < 3:
    counter += 1
    roll_dice(5 - len(numbers))
    draw_dices(numbers)
    print(is_game(find_repeated()))
    pick_dice()
    a = input("Tiras de nuevo? s/n")
    if a == "n":
        break



















