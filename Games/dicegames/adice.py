import random as rd

class Dice():
    "A dice to play dice games or simply have fun on the terminal"

    empty = "           "
    border = "+ ------- +"
    left_mark = "| x       |"
    right_mark = "|       x |"
    double_mark = "| x     x |"
    center_mark = "|    x    |"
    null_mark = "|         |"

    faces = {1: [empty, border, null_mark, center_mark, null_mark, border, empty],
                2: [empty, border, left_mark, null_mark, right_mark, border, empty],
                3: [empty, border, left_mark, center_mark, right_mark, border, empty],
                4: [empty, border, double_mark, null_mark, double_mark, border, empty],
                5: [empty, border, double_mark, center_mark, double_mark, border, empty],
                6: [empty, border, double_mark, double_mark, double_mark, border, empty]}

    #El estado del dado consiste en un número y una lista de líneas para dibujarlo.
    def __init__(self):
        self.value = rd.randint(1,6)
        self.lines = self.get_dice_lines()

    #Una función para actualizar la lista de líneas. Tener en cuenta que el diccionario faces y las distintas líneas
    #(empty, border, etc.) son compartidos por todas las intancias de la clase.
    def get_dice_lines(self):
        return Dice.faces[self.value]

    #El dado se sabe dibujar a sí mismo...
    def __str__(self):
        m = ""
        for l in range(7):
            m += self.draw_line(l)
            if l < 6:
                m += "\n"
        return m

    #Una función para dibujar una sola línea del dado y poder dibujar varios dados después...
    def draw_line(self, l):
        return self.lines[l] + " "

    #Una función para hacer trampa
    def set(self, n):
        self.value = n
        self.lines = self.get_dice_lines()

    #La función para tirar el dado
    def roll(self):
        self.value = rd.randint(1,6)
        self.lines = self.get_dice_lines()
