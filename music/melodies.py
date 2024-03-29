from music21 import *

#Some functions to play with music21 library

#A function to create a melody from a list
def list_stream(notes, center, duration_v):
	d = duration.Duration(duration_v)
	s = stream.Stream()
	for n in notes:
		new_note = note.Note(n + center)
		new_note.duration = d
		s.append(new_note)
	return s

#Function to create different duration values
def get_duration_values(count):
	durations_list = []
	for i in range(count):
		durations_list.append(duration.Duration((i+1)/4))
	return durations_list

#Functions to create tuplet
def get_tuplet(center, notes, denominator, type):
	t = duration.Tuplet(len(notes), denominator, type)
	s = stream.Stream()
	for n in notes:
		if not n == -1:
			new_note = note.Note(n + center)
		else:
			new_note = note.Rest()
		new_note.duration.appendTuplet(t)
		new_note.duration.type = type
		s.append(new_note)
	return s

def get_denominator_and_type(note_count):
	if note_count < 4:
		return 2, "eighth"
	elif note_count < 8:
		return 4, "16th"
	elif note_count < 16:
		return 8, "32nd"
	elif note_count < 32:
		return 16, "64th"
	else:
		return 32, "128th"
