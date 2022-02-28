from music21 import *
import randommelodies as rm
import random as rd
import melodies

the_list = [4,6,8,6,4,3,
			11,13,10,6,8,5,3,1,
			0,1,3,5,8,6,10,13,
			11,3,4,6,8,6,4,3,
			11,13,10,6,8,5,3,1,
			0,1,3,5,8,6,10,13,
			11,3,4,6,8,6,4,3]

the_list_2 = [0,2,4,6,8,10,0,4,8,2,0,4,6,10,2,
			4,6,8,10,0,2,4,8,0,6,4,8,10,2,6,8,10,0,
			2,4,6,8,0,4,10,8,0,2,4,10,
			0,2,4,6,8,10,0,4,8,2,0,4,6,10,2,
			4,6,8,10]

the_list_3 = [4, 9, 4, 9, 5, 2, 2, 2, 11, 7, 1, 5, 10, 5, 4, 11]
the_list_4 = [7, 7, 3, 4, 3, 10, 8, 5, 12, 6, 9, 6, 7, 9, 4, 10]

center = 60

bases = ["eighth","16th","32nd","64th"]
factor = [2,4,8,16]
notes = [-1,0,1,2,3,4,5,6,7,8,9,10,11]

s = stream.Stream()
s.append(meter.TimeSignature('3/4'))
s.append(tempo.MetronomeMark(number=34))
for i in range(25):
	size = rd.choice([3,5,6,7,9,10,11,13,14,15,16,17,19,21,23])
	n = []
	for v in range(size):
		n.append(rd.choice(notes))
	denominator, type = melodies.get_denominator_and_type(len(n))
	s.append(melodies.get_tuplet(center,n,denominator,type))

s.show()
