#Some functions to get musical scales

#Data we need
note_names = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "Sib", "Si"]
note_names_dict = {
	"Do": 0,
	"Do#": 1,
	"Reb": 1,
	"Re": 2,
	"Re#": 3,
	"Mib": 3,
	"Mi": 4,
	"Fa": 5,
	"Fa#": 6,
	"Solb": 6,
	"Sol": 7,
	"Sol#": 8,
	"Lab": 8,
	"La": 9,
	"La#": 10,
	"Sib": 10,
	"Si": 11
}
scale_patterns_up = { #Some ascending scale patterns
	"major": [0,2,4,5,7,9,11],
	"antique": [0,2,3,5,7,8,10],
	"harmonic": [0,2,3,5,7,9,10],
	"melodic": [0,2,3,5,7,9,11],
}
scale_patterns_down = { #Some descending scale patterns
	"major": [0,2,4,5,7,9,11],
	"antique": [0,2,3,5,7,8,10],
	"harmonic": [0,2,3,5,7,9,10],
	"melodic": [0,2,3,5,7,8,10]
}

#Function to translate note names into numbers
def translate_note(name):
	return note_names_dict[name]

#Function to print the notes from a scale
def print_scale(note_list):
	scale_text = "The notes are: "
	for i in range(len(note_list)):
		scale_text += note_names[note_list[i]] + " "
	print(scale_text, end="\n")

#A function to print an ascending scale
def scale_up(note, type):
	first_note = translate_note(note)
	pattern = scale_patterns_up[type]
	scale = []
	for i in range(len(pattern)):
		scale.append((first_note + pattern[i])%12)
	print_scale(scale)

#A function to print an descending scale
def scale_down(note, type):
	first_note = translate_note(note)
	pattern = scale_patterns_down[type]
	scale = []
	for i in range(len(pattern)):
		scale.append((first_note + pattern[len(pattern)-1-i])%12)
	print_scale(scale)
