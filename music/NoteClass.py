note_num = {"Do": (0, 0), "Do#": (0, 1), "Reb": (1, 1), "Re": (1, 2), "Re#": (1, 3),
           "Mib": (2, 3), "Mi": (2, 4), "Mi#": (2, 5), "Fa": (3, 5), "Fab": (3, 4),
           "Fa#": (3, 6), "Solb": (4, 6), "Sol": (4, 7), "Sol#": (4, 8), "Lab": (5, 8),
           "La": (5, 9), "La#": (5, 10), "Sib": (6, 10), "Si": (6, 11), "Dob": (0, 11),
           "Si#": (6, 0)}

num_note = {(0, 0): "Do", (0, 1): "Do#", (1, 1): "Reb", (1, 2): "Re", (1, 3): "Re#",
            (2, 3): "Mib", (2, 4): "Mi", (2, 5):"Mi#", (3, 5): "Fa", (3, 4): "Fab",
            (3, 6): "Fa#", (4, 6): "Solb", (4, 7): "Sol", (4, 8): "Sol#", (5, 8): "Lab",
            (5, 9): "La", (5, 10): "La#", (6, 10): "Sib", (6, 11): "Si", (0, 11): "Dob",
            (6, 0): "Si#"}

intervals = {"2m": [1, 1], "2M": [1, 2], "3m": [2, 3], "3M": [2, 4], "4J": [3, 5], "5J": [4, 7],
             "6m": [5, 8], "6M": [5, 9], "7m": [6, 10], "7M": [6, 11], "8J": [0, 0]}


num_interval = {(1, 1): "2m", (1, 2): "2M", (2, 3): "3m", (2, 4): "3M", (3, 5): "4J", (4, 7): "5J",
                (5, 8): "6m", (5, 9): "6M", (6, 10): "7m", (6, 11): "7M", (7, 0): "8J"}


class Note:
    """And Bach said: "Let there be notes"; and there where notes"""

    def __init__(self, n):
        self.nrlist = note_num[n]

    def __str__(self):
        return "No se que nombre me pusieron, pero....." + "\n" \
        "estoy segura de que soy un: " + num_note[self.nrlist]

    def transpose_up(self, i):
        int_num = intervals[i]
        new_note = (((self.nrlist[0] + int_num[0]) % 7), ((self.nrlist[1] + int_num[1]) % 12)) #No sabes la de veces que revise los parentesis
        self.nrlist = new_note

    def transpose_down(self, i):
        int_num = intervals[i]
        new_note = [(self.nrlist[0] - int_num[0]), (self.nrlist[1] - int_num[1])] #Lo hago lista porque la tupla es inmutable
        if new_note[0] < 0:
            new_note[0] += 7 #Entonces no me deja hacer estas opercaiones
        if new_note[1] < 0:
            new_note[1] += 12
        new_note = tuple(new_note) #Y hago esto porque sino el diccionario no camina, tiene que ser una tupla
        self.nrlist = new_note


class Interval:
    """Then Bach said: "Let there be intervals, an allow the notes to form couples"; and it was so"""

    def __init__(self, note1, note2):
        self.n1 = Note(note1)
        self.n2 = Note(note2)

    def distance(self,): #Para saber la distancia entre las notas del intervalo
        dst_num = [(self.n2.nrlist[0] - self.n1.nrlist[0]), (self.n2.nrlist[1] - self.n1.nrlist[1])]
        if dst_num[0] < 0:
            dst_num[0] += 7
        if dst_num[1] < 0:
            dst_num[1] += 12
        dst_num = tuple(dst_num)
        dst = num_interval[dst_num]
        return dst

    def inversion(self):
        inv = (self.n1.nrlist, self.n2.nrlist)
        self.n1 = Note(num_note[inv[1]])
        self.n2 = Note(num_note[inv[0]])

    def __str__(self):
        return "Mis Notas dicen: " + "\n" + str(self.n1) + "\n" + str(self.n2) + "\n" \
                "y mido una: " + self.distance()




