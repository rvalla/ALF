#Asi importamos tu flamante clase
from NoteClass import Note

#Explicamos lo que vamos a hacer...
print("-- Hola, espero que estés bien.", end="\n")
print("-- Vamos a probar la clase Note.", end="\n")
print("-- Voy a crear una nota 'DO'...", end="\n")
#Instanciamos una nota Do
do = Note("Do")
print("-- ¿No la ves? Ok, la imprimo", end="\n")
print("--", end="\n")
#Cuando imprimís un objeto o bien se imprime el tipo de objeto o bien se llama la función __str__ si existe
print(do)
print("", end="\n")

print("-- Probamos transportar...", end="\n")
print("-- Primero miramos los atributos de Do:", end="\n")
print(str(do.number), end="\n")
print(str(do.crom), end="\n")
print("-- Transportamos...", end="\n")
do.interval_up("6M")
print("-- Volvemos a mirar los atributos de Do:", end="\n")
print(str(do.number), end="\n")
print(str(do.crom), end="\n")
print("", end="\n")

print("-- La prueba ha concluido", end="\n")
