from music21 import *
import random as random

#Some functions to play with music21 library

#A function to create a totally random melody
def random_stream(notes_count, durations, low_limit, high_limit):
	duration_values = get_duration_values(durations)
	note_stream = stream.Stream()
	for n in range(notes_count):
		n = note.Note(random.randint(low_limit, high_limit))
		n.duration = random.choice(duration_values)
		note_stream.append(n)
	note_stream.show()

#A function to create a melody with a triangular distribution of pitches
def triangular_stream(notes_count, durations, low_limit, high_limit, mode_pitch):
	if low_limit < mode_pitch < high_limit:
		duration_values = get_duration_values(durations)
		note_stream = stream.Stream()
		for n in range(notes_count):
			n = note.Note(round(random.triangular(low_limit, high_limit, mode_pitch)))
			n.duration = random.choice(duration_values)
			note_stream.append(n)
		note_stream.show()
	else:
		print("The mode pitch is out of range!", end="\n")

#Function to create a melody with pitches in pitch_values control list
def control_stream(notes_count, durations, pitch_values):
	duration_values = get_duration_values(durations)
	note_stream = stream.Stream()
	for n in range(notes_count):
		n = note.Note(random.choice(pitch_values))
		n.duration = random.choice(duration_values)
		note_stream.append(n)
	note_stream.show()

#Function to create different duration values
def get_duration_values(count):
	durations_list = []
	for i in range(count):
		durations_list.append(duration.Duration((i+1)/4))
	return durations_list
