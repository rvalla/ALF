class GeneralaScore:

    col1 = ["Game", 1, 2, 3, 4, 5, 6,
            "Escalera", "Full", "Poker", "Generala", "Generala Doble"]
    line = "+--------------"

    def __init__(self, *args):
        self.players = list(args)
        self.table = self.create_table()

    def create_table(self):
        table = dict.fromkeys(self.col1, 0)
        for r in self.col1:
            if r == "Game":
                table[r] = self.players
            else:
                table[r] = [0 for i in range(len(self.players))]
        return table

    def input(self, p, g, n):# Me hace quilombo, da el valor n a todos los juegos
        self.table[g][self.table["Game"].index(p)] = n

    def __str__(self):
        l = ""
        for i in self.table:
            l += "|" + "{:^14}".format(i)
            for j in self.table[i]:
                l += "|" + "{:^14}".format(j)
            l += "\n"
            for k in range(len(self.players) + 1):
                l += self.line
            l += "\n"
        return l

a = GeneralaScore("Rodri", "Augusto", "ALF", "Pepe")
print(a)
a.input("Rodri", 1, 4)
a.input("Rodri", "Poker", 40)
a.input("Rodri", 5, 10)
a.input("Augusto", 3, 9)
a.input("ALF", 2, 4)
a.input("ALF", "Generala", 50)
print(a)
