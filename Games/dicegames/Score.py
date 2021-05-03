class Score():

    games = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [],
             "Escalera": [], "Full": [], "Poker": [], "Generala": [], "Generala doble": []}



    def __init__(self, *args):
        self.players = list(args)


    def create_dict(self):
        for i in Score.games:
            for p in self.players:
                self.games[i].append(0)


    def __str__(self):
        col1 = ["     Juego     |", "      1        |", "      2        |", "      3        |", "      4        |",
                "      5        |", "      6        |", "   Escalera    |", "     Full      |", "    Poker      |",
                "   Generala    |", "Generala doble |"]

        col2 = [self.players[0], self.games[1], self.games[2], self.games[3], self.games[4],
                self.games[5], self.games[6], self.games["Escalera"], self.games["Full"],
                self.games["Poker"], self.games["Generala"], self.games["Generala doble"]]

        horizontal = " ------------- |"

        t = ""
        for i in range(11):
            t += col1[i] + str(col2[i]) + "\n" + horizontal + horizontal + "\n"
        return t








a = Score("ALF", "Rodri", "Lolo")
print(a.players)
print(a)
a.create_dict()
print(a.games)


