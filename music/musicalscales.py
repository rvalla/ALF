#Some functions to get musical scales

#Data we need
note_names = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"]
note_classes = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "Sib", "Si"]
note_centers_up = [0,2,4,5,7,9,11]
note_centers_down = [0,11,9,7,5,4,2]
note_offsets = ["", "#", "##", "###", "*", "*", "*", "*", "*", "bbb", "bb", "b"]
note_names_dict = {
	"Dob": 0, "Do": 0, "Do#": 0, "Reb": 1, "Re": 1, "Re#": 1,
	"Mib": 2, "Mi": 2, "Mi#": 2, "Fab": 3, "Fa": 3, "Fa#": 3,
	"Solb": 4, "Sol": 4, "Sol#": 4,	"Lab": 5, "La": 5, "La#": 5,
	"Sib": 6, "Si": 6, "Si#": 6
}
scale_names_dict = {
	"Dob": 11, "Do": 0, "Do#": 1, "Reb": 1, "Re": 2, "Re#": 3,
	"Mib": 3, "Mi": 4, "Mi#": 5, "Fab": 4, "Fa": 5, "Fa#": 6,
	"Solb": 6, "Sol": 7, "Sol#": 8,	"Lab": 8, "La": 9, "La#": 10,
	"Sib": 10, "Si": 11, "Si#": 0
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
		return scale_names_dict[name], note_names_dict[name]
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
	note_class, note_value = translate_note(note)
	pattern = scale_patterns_up[type]
	return note_value, transpose_notes(pattern, note_class)

#A function to build an descending scale
def scale_down(note, type):
	note_class, note_value = translate_note(note)
	pattern = scale_patterns_down[type]
	return note_value, transpose_notes(pattern, note_class)

#Functions to print scales with correct names
def print_notes(note_class, note_l, direction, note_n, note_c):
	scale_text = "The notes are: "
	for i in range(7):
		new_note = ""
		p = ((i * direction) + note_class) % 7 #The position of the note in the seven notes list
		new_note += note_n[p]
		o = (note_l[i] - note_c[p]) % 12
		new_note += note_offsets[o]
		if i < 6:
			new_note += ", "
		scale_text += new_note
	return scale_text

#Function to print the notes from a scale
def print_notes_12(note_list):
	scale_text = "The notes are: "
	for i in range(len(note_list)):
		scale_text += note_classes[note_list[i]%12] + " "
	print(scale_text, end="\n")

#Function to print an ascending scale
def print_scale_up(note, type):
	scale_data = scale_up(note, type)
	return print_notes(scale_data[0], scale_data[1], 1, note_names, note_centers_up)

#A function to print an descending scale
def print_scale_down(note, type):
	scale_data = scale_down(note, type)
	return print_notes(scale_data[0], scale_data[1], -1, note_names, note_centers_up)

#A function to print a bidirectional scale
def print_scale_up_and_down(note, type):
	scale_text = ""
	scale_data = scale_up(note, type)
	scale_text += print_notes(scale_data[0], scale_data[1], 1, note_names, note_centers_up)
	scale_data = scale_down(note, type)
	scale_text += print_notes(scale_data[0], scale_data[1], -1, note_names, note_centers_down)
	return scale_text

#A function to print transposed notes
def print_transpose_notes(list, distance):
	note_list = translate_list(list)
	print_notes(transpose_notes(note_list, distance))
