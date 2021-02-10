from music21 import *
import random as random

class RandomMelodies():
	"Some functions to play with music21 library"

	notes_count = None #The number of notes to generate
	durations_count = None #The number of different note duration values
	durations_values = [] #The list of possible duration values
	pitch_values = [] #Possible midi pitch values for control_stream function
	high_limit = None #Midi value
	low_limit = None #Midi value

	#The constructor loads the user configuration
	def __init__(self, count, durations, pitches, l_limit, h_limit):
		RandomMelodies.notes_count = count
		RandomMelodies.durations_count = durations
		RandomMelodies.durations_values = RandomMelodies.get_duration_values(RandomMelodies.durations_count)
		RandomMelodies.pitch_values = pitches
		RandomMelodies.low_limit = l_limit
		RandomMelodies.high_limit = h_limit

	#A function to create a totally random melody
	def random_stream(self):
		note_stream = stream.Stream()
		for n in range(RandomMelodies.notes_count):
			n = note.Note(random.randint(RandomMelodies.low_limit, RandomMelodies.high_limit))
			n.duration = random.choice(RandomMelodies.durations_values)
			note_stream.append(n)
		note_stream.show()

	#A function to create a melody with a triangular distribution of pitches
	def triangular_stream(self, mode_pitch):
		if RandomMelodies.low_limit < mode_pitch < RandomMelodies.high_limit:
			note_stream = stream.Stream()
			for n in range(RandomMelodies.notes_count):
				n = note.Note(round(random.triangular(RandomMelodies.low_limit, RandomMelodies.high_limit, mode_pitch)))
				n.duration = random.choice(RandomMelodies.durations_values)
				note_stream.append(n)
			note_stream.show()
		else:
			print("The mode pitch is out of range!", end="\n")

	#Function to create a melody with pitches in pitch_values control list
	def control_stream(self, ):
		note_stream = stream.Stream()
		for n in range(RandomMelodies.notes_count):
			n = note.Note(random.choice(RandomMelodies.pitch_values))
			n.duration = random.choice(RandomMelodies.durations_values)
			note_stream.append(n)
		note_stream.show()

	#Function to create different duration values
	def get_duration_values(count):
		durations_list = []
		for i in range(count):
			durations_list.append(duration.Duration((i+1)/4))
		return durations_list
