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
            self.set_one(v, values[v])

    def set_some(self, values, dice_list):
        for v, d in zip(values, dice_list):
            self.set_one(d, v)

    def set_one(self, d, v):
        self.dice[d].set(v)
        self.update_vector_position(self.dice[d]) #Actualizamos el vector con la nueva información del dado que cambia

    #Las funciones para tirar los dados (todos o algunos)
    def roll_all(self):
        for d in range(len(self.dice)):
            self.roll_some(d)

    def roll_some(self, *args):
        for i in args:
            self.dice[i].roll()
            self.update_vector_position(self.dice[i])

    #def roll_some(self, dice_list):
     #   for d in dice_list:
      #      self.roll_one(d)

    #def roll_one(self, d):
     #   self.dice[d].roll()
      #  self.update_vector_position(self.dice[d])  #Actualizamos el vector con la nueva información del dado que cambia

    #La función que actualiza un dado en el vector eliminando el valor viejo y agregando el nuevo.
    def update_vector_position(self, dice):
        self.vector[dice.old_value - 1] -= 1 #Eliminamos el registro del valor anterior
        self.vector[dice.value - 1] += 1 #Registramos el nuevo valor

    #Una función para devolver los valores del conjunto de dados
    def get_dice_values(self):
        values = []
        for d in self.dice:
            values.append(d.value)
        return values

    #Esta función sólo crea el vector con 0s del tamaño que le digas (por si en algún momento hay dados con más caras)
    def get_new_vector(self, n):
        vector = [0 for i in range(n)]
        for d in self.dice:
            vector[d.value - 1] += 1 #Acá guardamos el estado del conjunto de dados (ojo con la posición 0)
        return vector
