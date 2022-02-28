from music21 import *

numerator =   [3,2,4,5,7,9,11,13,15,19,21]
denominator = [2,3,3,4,8,8,8,16,16,16,16]
types = ["eighth","eighth","eighth","16th","32nd","32nd","32nd","64th","64th","64th","64th"]
compas = ["2/4","6/8","6/8","2/4","2/4","2/4","2/4","2/4","2/4","2/4","2/4"]

s = stream.Stream()
for i in range(len(numerator)):
	s.append(meter.TimeSignature(compas[i]))
	s.staffLines = 1
	t = duration.Tuplet(numerator[i], denominator[i], types[i]) #Le podés pasar el tipo directamente...
	s.repeatAppend(note.Note(72, quarterLength=1),3)
	new_note = note.Note(72)
	new_note.duration.appendTuplet(t)
	new_note.duration.type = types[i]
	s.repeatAppend(new_note, numerator[i])
	print(t.totalTupletLength()) #Sirve para chequear cuánto suma el grupo de valores completo

s.show()
