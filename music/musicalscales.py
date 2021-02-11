#Some functions to get musical scales

#Data we need
note_names = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "Sib", "Si"]
note_names_dict = {
	"Do": 0, "Do#": 1, "Reb": 1, "Re": 2,
	"Re#": 3, "Mib": 3, "Mi": 4, "Fa": 5,
	"Fa#": 6, "Solb": 6, "Sol": 7, "Sol#": 8,
	"Lab": 8, "La": 9, "La#": 10, "Sib": 10,
	"Si": 11
}
scale_patterns_up = { #Some ascending scale patterns
	"major": [0,2,4,5,7,9,11],
	"antique": [0,2,3,5,7,8,10],
	"harmonic": [0,2,3,5,7,9,10],
	"melodic": [0,2,3,5,7,9,11],
}
scale_patterns_down = { #Some descending scale patterns
	"major": [0,11,9,7,5,4,2],
	"antique": [0,10,8,7,5,3,2],
	"harmonic": [0,10,9,7,5,3,2],
	"melodic": [0,10,8,7,5,3,2],
}

#Function to translate note names into numbers
def translate_note(name):
	try:
		return note_names_dict[name]
	except:
		print("I couldn't translate that note!", end="\n")

#Function to translate note lists into lists of numbers
def translate_list(note_list):
	new_list = []
	for i in range(len(note_list)):
		new_list.append(translate_note(note_list[i]))
	return new_list

#A function to tranpose notes
def transpose_notes(note_list, distance):
	new_list = []
	for i in range(len(note_list)):
		new_list.append(note_list[i] + distance)
	return new_list

#A function to build an ascending scale
def scale_up(note, type):
	first_note = translate_note(note)
	pattern = scale_patterns_up[type]
	return transpose_notes(pattern, first_note)

#A function to build an descending scale
def scale_down(note, type):
	first_note = translate_note(note)
	pattern = scale_patterns_down[type]
	return transpose_notes(pattern, first_note)

#A function to build a bidirectional scale
def scale_up_and_down(note, type):
	scale = scale_up(note, type)
	scale += scale_down(note, type)
	return scale

#Function to print the notes from a scale
def print_notes(note_list):
	scale_text = "The notes are: "
	for i in range(len(note_list)):
		scale_text += note_names[note_list[i]%12] + " "
	print(scale_text, end="\n")

#Function to print an ascending scale
def print_scale_up(note, type):
	print_notes(scale_up(note, type))

#A function to print an descending scale
def print_scale_down(note, type):
	print_notes(scale_down(note, type))

#A function to print a bidirectional scale
def print_scale_up_and_down(note, type):
	print_notes(scale_up_and_down(note, type))

#A function to print transposed notes
def print_transpose_notes(list, distance):
	note_list = translate_list(list)
	print_notes(transpose_notes(note_list, distance))
