from diceset import DiceSet
from generala import Generala

class Match():

    def __init__(self, *players):
        self.players = self.build_players(players)
        self.p_count = len(self.players) #La cantidad de jugadores
        self.p_active = 0
        self.r_count = 0 #La cantidad de tiradas para distinguir juegos "servidos"
        self.ds = DiceSet(5)
        self.play()

    #Acá hay que armar el juego...
    def play(self):
        self.ds.roll_all()
        print(self.ds)
        self.players[self.p_active].set_play("Juego", "Póker", 2)

    #Construimos los jugadores
    def build_players(self, names):
        p = []
        for n in names:
            p.append(Generala(n))
        return p

    #Como Dice imprime una  línea de la tabla
    def draw_line(self, l):
        line = ""
        line += self.players[0].plays_names[l] + "\t"
        for p in self.players:
            line += p.draw_line(l) + "\t"
        return line

    #Sólo imprime el estado del juego de un jugador con su nombre
    def __str__(self):
        m = ""
        for l in range(13):
            m += self.draw_line(l)
            if l < 12:
                m += "\n"
        return m
