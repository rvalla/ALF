from music21 import *

#Some functions to create a melody from durations and notes lists

def circle_melody(note_list, duration_list):
	nc = len(note_list) #Miramos la cantidad de notas
	dc = len(duration_list) #Miramos la cantidad de duraciones
	notes = lowest_multiple(nc, dc) #Buscamos el mínimo común múltiplo de nc y dc
	note_stream = stream.Stream()
	for n in range(notes):
		new_note = note.Note(note_list[n%nc]) #Agregamos la nota
		new_note.duration = duration.Duration(duration_list[n%dc]) #Agregamos la duración
		note_stream.append(new_note)
	note_stream.show()

#Necesitamos buscar el mínimo común múltiplo entre dos números
#Vamos a buscarlo sabiendo que un múltiplo de b es divisible por b
def lowest_multiple(a, b):
	n = 1
	for i in range(1, b + 1, 1):
		n = a * i #Vamos recorriendo los múltiplos de a
		if (n%b == 0):
			break #Nos quedamos con el mínimo que también es múltiplo de b
	return n
