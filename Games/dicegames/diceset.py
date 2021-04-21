from adice import Dice

class DiceSet():
    "A dice set to play"

    #El estado del dado consiste en un número y una lista de líneas para dibujarlo.
    def __init__(self, n):
        self.dice = self.build_dice(n)
        self.vector = self.get_new_vector(6) #Acá dejo el vector para guardar el juego.

    def build_dice(self, n):
        d = []
        for i in range(n):
            d.append(Dice())
        return d

    #Los dados se dibujan a sí mismos...
    def __str__(self):
        m = ""
        for l in range(7):
            for d in self.dice:
                m += d.draw_line(l)
                m += " "
            if l < 6:
                m += "\n"
        return m

    #Las funciones para hacer trampa (con todos o algunos)
    def set_all(self, values):
        for v in range(len(values)):
            self.dice[v].set(values[v])

    def set_some(self, values, dice_list):
        for v, d in zip(values, dice_list):
            self.set_one(d, v)

    def set_one(self, d, v):
        self.dice[d].set(v)

    #Las funciones para tirar los dados (todos o algunos)
    def roll_all(self):
        for d in self.dice:
            d.roll()

    def roll_some(self, dice_list):
        for d in dice_list:
            self.roll_one(d)

    def roll_one(self, d):
        self.dice[d].roll()

    #Una función para devolver los valores del conjunto de dados
    def get_dice_values(self):
        values = []
        for d in self.dice:
            values.append(d.value)
        return values

    def get_new_vector(self, n):
        return [0 for i in range(n)]
