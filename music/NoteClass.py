# Para entender esta garompa:
# A pedido del gran maese estamos volviendo a representar las notas con numeros y operar con ellos.
# A tal fin propongo representarlas con dos numeros como si fueran ccordenadas (aunque no los son, creo)
# El primer numero del par nos dice el "nombre" de la nota do, re, mi ,fa etc entonces son numeros del 0 al 6
# El segundo numero nos dice la ubicacion del sonido en el "escpacio cromatico" do, do#, re, re# etc. entonces van
# del 0 al 11
# Ergo, por ejemplo la nota Re# va a tener el par de numeros (2, 3) el Mi (2, 5) etc.
# Esto nos permite operar con estos numeros coordenada subiendo y bajando "nombres de nota" o "espacios cromaticos"
# muy esoterico pero asi lo imagino yo

# Entonces: Habra diccionarios!!! si!!!! que lleven el nombre de la nota a coordenadas y al reves ya que no me gutaria
# tener que crear una nota que se llame (2,5) prefiero decirle Mi y tampoco me gustaría que el programa me conteste asi.
# Es una cuestion de buenos modales
# Hay tambien un diccionario que nos dice que numeros hay que sumar o restar para subir o bajar  determinado intervalo
# Y otro que hace el camino inverso porquetambien me parecio interesante que tiremos dos notas y nos diga el intervalo.

note_num = {"Do": [0, 0], "Do#": [0, 1], "Reb": [1, 1], "Re": [1, 2], "Re#": [1, 3],
           "Mib": [2, 3], "Mi": [2, 4], "Mi#": [2, 5], "Fa": [3, 5], "Fab": [3, 4],
           "Fa#": [3, 6], "Solb": [4, 6], "Sol": [4, 7], "Sol#": [4, 8], "Lab": [5, 8],
           "La": [5, 9], "La#": [5, 10], "Sib": [6, 10], "Si": [6, 11], "Dob": [0, 11],
           "Si#": [6, 0]}

# Para que los "Keys" del diccionario puedan ser estos pares de nros deben ser tuplas y no listas. WTFFFFF???? Entiendo, no soy especialista en diccionarios.
num_note = {(0, 0): "Do", (0, 1): "Do#", (1, 1): "Reb", (1, 2): "Re", (1, 3): "Re#",
            (2, 3): "Mib", (2, 4): "Mi", (2, 5):"Mi#", (3, 5): "Fa", (3, 4): "Fab",
            (3, 6): "Fa#", (4, 6): "Solb", (4, 7): "Sol", (4, 8): "Sol#", (5, 8): "Lab",
            (5, 9): "La", (5, 10): "La#", (6, 10): "Sib", (6, 11): "Si", (0, 11): "Dob",
            (6, 0): "Si#"}

intervals = {"2m": [1, 1], "2M": [1, 2], "3m": [2, 3], "3M": [2, 4], "4J": [3, 5], "5J": [4, 7],
             "6m": [5, 8], "6M": [5, 9], "7m": [6, 10], "7M": [6, 11], "8J": [0, 0]} #Corrijo el 7 acá

# Agregate unos intervalos si queres, yo ya perdi la vista

num_interval = {(1, 1): "2m", (1, 2): "2M", (2, 3): "3m", (2, 4): "3M", (3, 5): "4J", (4, 7): "5J",
                (5, 8): "6m", (5, 9): "6M", (6, 10): "7m", (6, 11): "7M", (7, 0): "8J"}

class Note:
    "Acá le podemos poner una linda descripción a la clase"
    # El constructor de la nota toma los dos valores de la lista dentro del diccionario y los separa para poder operar
    # No sera necesario separarlos? en mi cabeza si pero por ahi es al pedo
    def __init__(self, n):
        nrlist = note_num[n] #esta queda como variable auxiliar, mirá que cuando instancies más de 1 cambia y no coincide*
        self.number = nrlist[0]
        self.crom = nrlist[1]

	#* creo que por ahí te conviene o guardar self.tupla con las dos cosas y también lo otro. Y decidir qué llamar según
	#lo que necesites. Debe ser más rápido consultar un número que un elemento en una tupla. (¿Se dirá tupla?)

	#Bueno, bueno. Estás bien orientado. Pero estos métodos no son lo que creo que necesitás. El metodo interval_up(n)
	#debería transformar la nota verdaderamente, cambiarle el estado. Cambiar los valores de self.number y self.crom y
	#no imprimir. De hecho no te conviene imprimir. De última te conviene devolver un string. Devería haber funciones
	#que cambien el estado de la nota y funciones que la impriman.

    # Pavadas que no requieren mucha explicacion
    def interval_up(self, int):
        int_numbers = intervals[int]
        new_number = (self.number + int_numbers[0]) % 7
        new_crom = (self.crom + int_numbers[1]) % 12
        print(num_note[new_number, new_crom])

    def interval_down(self, int):
        int_numbers = intervals[int]
        new_number = self.number - int_numbers[0]
        if new_number < 0:  # No encontre un modo mas elegante de resolver esto que los condicionales. dibuje maestro
            new_number += 7
        new_crom = self.crom - int_numbers[1]
        if new_crom < 0:
            new_crom += 12
        print(num_note[new_number, new_crom])

    def get_interval(self, n2):
        new_number = n2.number - self.number
        new_crom = n2.crom - self.crom
        print(num_interval[new_number, new_crom])

    def __str__(self):
        return "Hola, yo soy una nota" + "\n" \
               "En este momento soy: " + \
               str(num_note[self.number, self.crom]) + "\n" + \
               "Y me encanta..."


#Esto lo vas a sacar de aquí... jeje
# Algunas notas creadas para probar
do = Note("Do")
dos = Note("Do#")
reb = Note("Reb")
fa = Note("Fa")
la = Note("La")

# Algunas llamaditas que hasta aca funcionan no quiero hacer mas pruebas por las dudas
dos.interval_up("2M")
do.interval_up("6M")
fa.interval_up("6M")
do.interval_up("8J")
dos.interval_up("8J")
do.interval_down("3m")
do.get_interval(fa)
fa.get_interval(la)
