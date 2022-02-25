from music21 import *
import randommelodies as rm
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

s = melodies.get_tuplet([0,-1,2,4,5],center,2,"eighth")
s.append(melodies.get_tuplet([0,1,2],center,1,"eighth"))
s.append(melodies.get_tuplet([0,1,2,4,5,6,5,4,5,3,3,1,0],center,1,"16th"))

s.show()
