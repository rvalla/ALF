#Asi importamos tu flamante clase
from NoteClass import Note
from NoteClass import Interval
from NoteClass import Scale
from NoteClass import Chord

#Explicamos lo que vamos a hacer...
print("-- Hola, espero que estés bien.", end="\n")
print("-- Vamos a probar la clases Note, Interval, Scale y Chord.", end="\n")
print("-- Están todas en el mismo archivo, y bue...", end="\n")

#Instanciamos una nota
print("------------------", end="\n")
print("-- Vamos con Note...", end="\n")
n = Note("Do")
print("-- ¿No la ves? Ok, la imprimo", end="\n")
print("--", end="\n")
#Cuando imprimís un objeto o bien se imprime el tipo de objeto o bien se llama la función __str__ si existe
print(n)
print("", end="\n")

print("-- Probamos transportar...", end="\n")
print("-- Primero miramos los atributos de Do:", end="\n")
print(str(n.nrlist[0]), end="\n")
print(str(n.nrlist[1]), end="\n")
print("-- Transportamos...", end="\n")
n.transpose("6M", "Up")
print("-- Volvemos a mirar los atributos de Do:", end="\n")
print(str(n.nrlist[0]), end="\n")
print(str(n.nrlist[1]), end="\n")
print(n)
print("", end="\n")

print("------------------", end="\n")
print("-- Vamos con Interval", end="\n")
i = Interval("Do", "Sol", "Up")
print(i)
print("", end="\n")
print("Transportamos...", end="\n")
i.transpose("6M", "Down")
print(i)
print("", end="\n")
print("Invertimos...", end="\n")
i.inversion()
print(i)
print("", end="\n")

print("------------------", end="\n")
print("Vamos con Scale...", end="\n")
s = Scale("Re", "Mayor")
print(s)
print("", end="\n")
print("Transportamos", end="\n")
s.transpose("2M", "Down")
print(s)
print("", end="\n")
print("Creamos la relativa...", end="\n")
sr = s.relative()
print(sr)
print("", end="\n")

print("------------------", end="\n")
print("Vamos con Chord...", end="\n")
c = Chord("Sol", "Mayor", "6")
print(c)
print("", end="\n")
print("Invertimos el acorde...", end="\n")
c.invert("6/4")
print(c)
print("", end="\n")
print("Transportamos...", end="\n")
c.transpose("3M", "Up")
print(c)
print("", end="\n")

print("Hemos concluido la prueba...", end="\n")
print("Muchas gracias", end="\n")
