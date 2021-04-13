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

intervals = {"1": [0, 0], "2m": [1, 1], "2M": [1, 2], "3m": [2, 3], "3M": [2, 4], "4J": [3, 5], "5J": [4, 7], "5Dim": [4,6],
             "6m": [5, 8], "6M": [5, 9], "7m": [6, 10], "7M": [6, 11], "8J": [7, 0]}


num_interval = {(1, 1): "2m", (1, 2): "2M", (2, 3): "3m", (2, 4): "3M", (3, 5): "4J", (4, 7): "5J", (4, 6): "5Dim",
                (5, 8): "6m", (5, 9): "6M", (6, 10): "7m", (6, 11): "7M", (7, 0): "8J"}

mod = {"Up": 1, "Down": -1}

mode_int = {"Mayor": ["1", "2M", "3M", "4J", "5J", "6M", "7M", "8J"],
                "Menor Antigua": ["1", "2M", "3m", "4J", "5J", "6m", "7m", "8J"],
                "Menor Melódica": ["1", "2M", "3m", "4J", "5J", "6M", "7M", "8J",
                                   "7m", "6m", "5J", "4J", "3m", "2M", "1"],
                "Menor Bachiana": ["1", "2M", "3m", "4J", "5J", "6M", "7M", "8J"],
                "Menor Armónica": ["1", "2M", "3m", "4J", "5J", "6m", "7m", "8J"],
                "Mayor Mixta Artificial": ["1", "2M", "3M", "4J", "5J", "6m", "7M", "8J"]}

chords_int = {"Mayor": ["1", "3M", "5J"], "Menor": ["1", "3m", "5J"], "Aumentado": ["1", "3M", "3M"],
              "Disminuido": ["1", "3m", "5Dim"]}

pos = {"Ef": 0, "6": 1, "6/4": 2}

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
        self.nrlist = ((self.nrlist[0] + (int_num[0] * mod[d])) % 7), ((self.nrlist[1] + (int_num[1] * mod[d])) % 12)

    def create_my(self, i, d):
        int_num = intervals[i]
        new_note = ((self.nrlist[0] + (int_num[0] * mod[d])) % 7), ((self.nrlist[1] + (int_num[1] * mod[d])) % 12)
        return Note(num_note[new_note])


class Interval:
    """Then Bach said: "Let there be intervals, an allow the notes to form couples"; and it was so"""

    def __init__(self, note1, note2, d):
        self.root = Note(note1)
        self.n2 = Note(note2)
        self.dir = d

    def distance(self):
        if self.dir == "Up":
            dst_num = ((self.n2.nrlist[0] - self.root.nrlist[0]) % 7), ((self.n2.nrlist[1] - self.root.nrlist[1]) % 12)
        if self.dir == "Down":
            dst_num = ((self.root.nrlist[0] - self.n2.nrlist[0]) % 7), ((self.root.nrlist[1] - self.n2.nrlist[1]) % 12)
        print(dst_num)
        dst = num_interval[dst_num]
        return dst

    def inversion(self):
        inv = (self.root.nrlist, self.n2.nrlist)
        self.root = Note(num_note[inv[1]])
        self.n2 = Note(num_note[inv[0]])

    def transpose(self, i, d):
        self.root.transpose(i, d)
        self.n2.transpose(i, d)

    def __str__(self):
        return "Mis Notas dicen: " + "\n" + str(self.root) + "\n" + str(self.n2) + "\n" \
                "Mi dirección es: " + self.dir + "\n" \
                "Y mido una: " + self.distance()

class Scale:
    """Later Bach created groups of notes and called them "scales" and Bach saw that this was good"""

    def __init__(self, root, mode):
        self.root_name = root
        self.root = Note(root)
        self.mode = mode
        self.mode_int = mode_int[self.mode]
        self.notes = []
        for i in mode_int[self.mode]:
            self.notes.append(self.root.create_my(i, "Up"))
        self.grades = self.create_scale_chords() #Ya que lo querés la escala conoce sus grados...

    def transpose(self, i, d):
        self.root.transpose(i, d)
        for n in self.notes:
            n.transpose(i, d)

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

    #Andrés wanted to save of chords in a scale so he did this:
    def create_scale_chords(self):
        grades = [] #Acá vas a guardar los acordes, ok
        chordnotes = []
        patr = [0, 2, 4] #Esta magia se puede aprovechar mejor
        aux = [] #Podría llamarse "Ouch!"

        #Ahora hay que recorrer las notas de la escala
        for i in range(7):
            notes = []
            for p in patr:
                notes.append(self.notes[(i + p)%7].name)
            grades.append(Chord(notes[0], Chord.guess_type(notes), "Ef"))

        #Esto que sigue se puede borrar...
        #def guess_notes():
        #    for i in patr:
        #        a = self.notes[i]
        #        chordnotes.append(a.name)

        #def guess_type(notes):
        #    int_chord = {("3M", "5J"): "Mayor", ("3m", "5J"): "Menor", ("3M", "5Aum"): "Aumentado",
        #                    ("3m", "5Dim"): "Disminuido"}
        #    distances = []
        #    a = Interval(notes[0], notes[1], "Up")
        #    b = Interval(notes[0], notes[2], "Up")
        #    distances.append(a.distance())
        #    distances.append(b.distance())
        #    distances = tuple(distances)
        #    return int_chord[distances]

        #def move_patr():
        #    for i in patr:
        #        aux.append((i + 1) % 7)
        #    for i in aux:
        #        patr.append(i)
        #    del patr[0: 3]
        #    aux.clear()

        #for i in range(len(self.notes)):
        #    guess_notes()
        #    i = Chord(chordnotes[0], guess_type(chordnotes), "Ef")
        #    grades.append(i)
        #    move_patr()
        #    chordnotes.clear()

        return grades

    def __str__(self):
        m = "Mis notas dicen: " + "\n"
        for n in self.notes:
            m += str(n) + "\n"
        return m

class Chord:
    """Soon after Bach arranged the notes by thirds, and he was pleased, so he called them "chords" """

    #Este diccionario va acá me parece...
    int_chord = {("3M", "5J"): "Mayor", ("3m", "5J"): "Menor", ("3M", "5Aum"): "Aumentado",
                        ("3m", "5Dim"): "Disminuido"}

    def __init__(self, root, type, p):
        self.root = Note(root)
        self.type = type
        self.pos = pos[p]
        self.notes = []
        for i in chords_int[type]:
            self.notes.append(self.root.create_my(i, "Up"))
        self.size = len(self.notes)
        for i in range(self.pos):
            self.notes.append(self.notes.pop(0))

    def invert(self, p):
        self.pos = pos[p]
        self.notes.clear()
        for i in chords_int[self.type]:
            self.notes.append(self.root.create_my(i, "Up"))
        for i in range(self.pos):
            self.notes.append(self.notes.pop(0))

    def transpose(self, i, d):
        self.root.transpose(i, d)
        for n in self.notes:
            n.transpose(i, d)

    #Mudo la función acá y la escribo más pequeña...
    def guess_type(notes):
        a = Interval(notes[0], notes[1], "Up")
        b = Interval(notes[0], notes[2], "Up")
        return Chord.int_chord[(a.distance(), b.distance())]

    def __str__(self):
        m = "Mis notas dicen: " + "\n"
        for i in range(len(self.notes)):
            m += str(self.notes[i]) + "\n"
        return m
