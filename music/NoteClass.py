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

intervals = {"1": [0, 0], "2m": [1, 1], "2M": [1, 2], "3m": [2, 3], "3M": [2, 4], "4J": [3, 5], "5J": [4, 7],
             "6m": [5, 8], "6M": [5, 9], "7m": [6, 10], "7M": [6, 11], "8J": [7, 0]}


num_interval = {(1, 1): "2m", (1, 2): "2M", (2, 3): "3m", (2, 4): "3M", (3, 5): "4J", (4, 7): "5J",
                (5, 8): "6m", (5, 9): "6M", (6, 10): "7m", (6, 11): "7M", (7, 0): "8J"}

mod = {"Up": 1, "Down": -1}

mode_int = {"Mayor": ["1", "2M", "3M", "4J", "5J", "6M", "7M", "8J"],
                "Menor Antigua": ["1", "2M", "3m", "4J", "5J", "6m", "7m", "8J"],
                "Menor Melódica": ["1", "2M", "3m", "4J", "5J", "6M", "7M", "8J",
                                   "7m", "6m", "5J", "4J", "3m", "2M", "1"],
                "Menor Bachiana": ["1", "2M", "3m", "4J", "5J", "6M", "7M", "8J"],
                "Menor Armónica": ["1", "2M", "3m", "4J", "5J", "6m", "7m", "8J"],
                "Mayor Mixta Artificial": ["1", "2M", "3M", "4J", "5J", "6m", "7M", "8J"]}

class Note:
    """And Bach said: "Let there be notes"; and there where notes"""

    def __init__(self, n):
        self.nrlist = note_num[n]
        self.name = n

    def __str__(self):
        return "No se que nombre me pusieron, pero....." + "\n" \
        "estoy segura de que soy un: " + num_note[self.nrlist]

    def transpose(self, i, d):
        int_num = intervals[i]
        new_note = ((self.nrlist[0] + (int_num[0] * mod[d])) % 7), ((self.nrlist[1] + (int_num[1] * mod[d])) % 12)
        self.nrlist = new_note

    def create_my(self, i, d):
        int_num = intervals[i]
        new_note = ((self.nrlist[0] + (int_num[0] * mod[d])) % 7), ((self.nrlist[1] + (int_num[1] * mod[d])) % 12)
        return Note(num_note[new_note])


class Interval:
    """Then Bach said: "Let there be intervals, an allow the notes to form couples"; and it was so"""

    def __init__(self, note1, note2, d):
        self.n1 = Note(note1)
        self.n2 = Note(note2)
        self.dir = d

    def distance(self):
        if self.dir == "Up":
            dst_num = ((self.n2.nrlist[0] - self.n1.nrlist[0]) % 7), ((self.n2.nrlist[1] - self.n1.nrlist[1]) % 12)
        if self.dir == "Down":
            dst_num = ((self.n1.nrlist[0] - self.n2.nrlist[0]) % 7), ((self.n1.nrlist[1] - self.n2.nrlist[1]) % 12)
        dst = num_interval[dst_num]
        return dst #Esto no lo estoy usando, lo puse por si hiciera falta. no me imagino ahora para que. lo dejarias?

    def inversion(self):
        inv = (self.n1.nrlist, self.n2.nrlist)
        self.n1 = Note(num_note[inv[1]])
        self.n2 = Note(num_note[inv[0]])

    def transpose(self, i, d):
        new_n1 = self.n1
        new_n1.transpose(i, d)
        new_n2 = self.n2
        new_n2.transpose(i, d)

    def __str__(self):
        return "Mis Notas dicen: " + "\n" + str(self.n1) + "\n" + str(self.n2) + "\n" \
                "Mi dirección es: " + self.dir + "\n" \
                "Y mido una: " + self.distance()

class Scale:
    """Later Bach created groups of notes and call them "scales" and Bach saw that this was good"""

    def __init__(self, root, mode):
        self.root_name = root #Al final no lo usé
        self.root = Note(root)
        self.mode = mode
        self.mode_int = mode_int[self.mode]
        self.notes = []
        for i in mode_int[self.mode]:
            self.notes.append(self.root.create_my(i, "Up"))

    def transpose(self, i, d):
        r = self.root
        r.transpose(i, d)
        self.notes.clear()
        for n in self.mode_int:
            self.notes.append(self.root.create_my(n, "Up"))

    def change_mode(self, m):
        self.mode = m
        self.notes.clear()
        for i in mode_int[self.mode]:
            self.notes.append(self.root.create_my(i, "Up"))

    def relative(self):
        if self.mode == "Mayor" or self.mode == "Mayor Mixta Artificial":
            mode = "Menor Antigua"
            new_root = self.root.create_my("3m", "Down")
            relative = Scale(new_root.name, mode)
        if self.mode == "Menor Antigua" or self.mode == "Menor Armónica" \
                or self.mode == "Menor Melódica" or self.mode == "Menor Bachiana":
            mode = "Mayor"
            new_root = self.root.create_my("3m", "Up")
            relative = Scale(new_root.name, mode)
        return relative

    def print(self): #No lo pude hacer imprimir bien con str.....
        print("Mis notas dicen: ")
        for i in range(len(self.notes)):
            print(self.notes[i])





