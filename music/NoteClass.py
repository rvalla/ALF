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

chords_int = {"Mayor": ["1", "3M", "5J"]}
pos = {"Ef": 0, "6": 1, "6/4": 2}

class Note:
    """And Bach said: "Let there be notes"; and there where notes"""

    def __init__(self, n):
        self.nrlist = note_num[n]
        self.name = n

    #Voy a ponerme serio acá así nos sirve... Fue divertido mientras duró.
    def __str__(self):
        return "No se que nombre me pusieron, pero....." + "\n" \
        "estoy segura de que soy un: " + num_note[self.nrlist]

    #Ok. Perdón. Pero cuando los programas crecen hay que ahorrar líneas. Voy a intervenir acá como ejemplo:
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
        self.n1 = Note(note1)
        self.n2 = Note(note2)
        self.dir = d

    def distance(self):
        if self.dir == "Up":
            dst_num = ((self.n2.nrlist[0] - self.n1.nrlist[0]) % 7), ((self.n2.nrlist[1] - self.n1.nrlist[1]) % 12)
        if self.dir == "Down":
            dst_num = ((self.n1.nrlist[0] - self.n2.nrlist[0]) % 7), ((self.n1.nrlist[1] - self.n2.nrlist[1]) % 12)
        dst = num_interval[dst_num]
        return dst #Esto no lo estoy usando, lo puse por si hiciera falta. no me imagino ahora para que. lo dejarias?**
        #MENTIRA: Lo está usando __str__ para imprimir la distancia.

    def inversion(self):
        inv = (self.n1.nrlist, self.n2.nrlist)
        self.n1 = Note(num_note[inv[1]])
        self.n2 = Note(num_note[inv[0]])

    #Intervengo acá también. Veo que usás expresiones de igualdad como trocados de contrapunto tonal. Pero la igualdad
    #es bidireccional. a = b es lo mismo que b = a, no es como en las fugas de Bach.
    def transpose(self, i, d):
        self.n1.transpose(i, d)
        self.n2.transpose(i, d)

    def __str__(self):
        return "Mis Notas dicen: " + "\n" + str(self.n1) + "\n" + str(self.n2) + "\n" \
                "Mi dirección es: " + self.dir + "\n" \
                "Y mido una: " + self.distance()

class Scale:
    """Later Bach created groups of notes and called them "scales" and Bach saw that this was good"""

    def __init__(self, root, mode):
        self.root_name = root #Al final no lo usé. Tenés el dato en la primera nota...
        self.root = Note(root)
        self.mode = mode
        self.mode_int = mode_int[self.mode]
        self.notes = []
        for i in mode_int[self.mode]:
            self.notes.append(self.root.create_my(i, "Up"))

    def transpose(self, i, d): #Esto es una aberración. Cualquiera...
        #r = self.root #Al pedo. Querés transportar toda la escala.
        #r.transpose(i, d) #Claro, también es al pedo
        #self.notes.clear() #What? Las notas se saben mover, ¿por qué creas notas de nuevo?
        #Fuck you. Si tus listas tuvieran 100.000 elementos armarías un embotellamiento. Qué piola... Como tenés listas
        #de 7 hacés cualquiera porque total la computadora lo hace rapidísimo...
        self.root.transpose(i,d)
        for n in self.notes:
            n.transpose(i,d) #Ya está. Perdón... Debo enfurecer menos.

    def change_mode(self, m): #este método debería llamarse change_scale...
        self.mode = m
        self.notes.clear() #Por este clear digo...
        for i in mode_int[self.mode]:
            self.notes.append(self.root.create_my(i, "Up"))

    def relative(self): #Epa... Groso
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

    def __str__(self): #No lo pude hacer imprimir bien con str..... ¿Llamaste a un método con un nombre que ya existe?***
        m = "Mis notas dicen: " + "\n"
        for n in self.notes:
            m += str(n) + "\n"
        return m #Este método tiene que devolver un string, si no no anda.
        #***print() es una función del lenguaje. Agregaste una de la clase, ok. A la larga te va a marear jajaja.

class Chord:
    """Soon after Bach arranged the notes by thirds, and he was pleased, so he called them "chords" """

    def __init__(self, root, type, p):
        self.root_name = root
        self.root = Note(root)
        self.type = type
        self.pos = pos[p] #Este número me lo guardo para imprimir nomás
        self.notes = []
        for i in chords_int[type]:
            self.notes.append(self.root.create_my(i, "Up")) #Ya está, contá los paréntesis. Es así.
        self.size = len(self.notes) #Me guardo la cantidad de notas que tiene
        #A la bosta lo que sigue
        #for i in range(self.pos):
        #    self.notes.append(self.notes.pop(0)) #Me dio un isquemia. No sé qué carajo querés acá.

    #def inv(self, p):
    #    self.pos = pos[p]
    #    for i in range(self.pos):
    #        self.notes.append(self.notes.pop(0))

    def invert(self, p):
        self.pos = pos[p]

    def transpose(self, i, d): #Vago, este no puede faltar*** jajajaja
        self.root.transpose(i,d)
        for n in self.notes:
            n.transpose(i,d)
    #***Si sumás root a Interval acá puede haber algo de herencia. El método transpose es igual para todos. 

    def __str__(self):
        m = "Mis notas dicen: " + "\n"
        for i in range(self.size):
            m += str(self.notes[(i + self.pos)%self.size]) + "\n"
        return m
