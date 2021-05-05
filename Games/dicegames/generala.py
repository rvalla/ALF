class Generala():

    plays_names = ["|  Juego   |",
                    "| -------- |",
                    "|     1    |",
                    "|     2    |",
                    "|     3    |",
                    "|     4    |",
                    "|     5    |",
                    "|     6    |",
                    "| Escalera |",
                    "|   Full   |",
                    "|   Póker  |",
                    "| Generala |",
                    "|  Doble   |"]

    plays_map = {"Escalera": 6, "Full": 7, "Póker": 8, "Generala": 9, "Doble": 10}
    points_map = {"Escalera": 20, "Full": 30, "Póker": 40, "Generala": 50, "Doble": 100}

    def __init__(self, player):
        self.player = player
        self.plays = [0,0,0,0,0,0,0,0,0,0,0]

    #Vamos con *args como a vos te gusta. Vamos a recibir categoría primero:
    #Categorías: "número", "juego"
    def set_play(self, *play):
        try:
            if play[0] == "Número":
                points = play[1] * play[2]
                self.plays[play[1] - 1] = points
            elif play[0] == "Juego":
                self.plays[self.plays_map[play[1]]] = self.points_map[play[1]]
                if play[2] == 1:
                    if play[1] == "Generala" or play[1] == "Doble":
                        self.plays[self.plays_map[play[1]]] += 1000
                    else:
                        self.plays[self.plays_map[play[1]]] += 5
        except:
            print("Ups...", end="\n")
            print("Fue imposible registrar la jugada", end="\n")

    #Como Dice imprime una  línea del estado del juego para poder armar la tabla con muchos
    def draw_line(self, l):
        if l == 0:
            return self.player
        if l == 1:
            return ""
        else:
            return str(self.plays[l - 2])

    #Sólo imprime el estado del juego de un jugador con su nombre
    def __str__(self):
        m = ""
        for l in range(13):
            print(l)
            m += self.plays_names[l] + " "
            m += self.draw_line(l)
            if l < 12:
                m += "\n"
        return m
