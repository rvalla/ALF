input = input("Give me a word to play with: ")

def print_word(word): #Esta función imprime y devuelve None (nada)
	print("-- " + word, end="\n")

def return_word(word):
	return "-- " + word + "\n" #Esta función no imprime, devuelve la palabra

def print_reverse(word): #Esta función imprime al revés y devuelve None
	print("-- " + word[::-1], end="\n")

def return_reverse(word):
	return "-- " + word[::-1] + "\n"

def print_with_check(word):
	isAuto = None #Las variables se pueden definir como None
	if word == "Auto":
		isAuto = True
	else:
		isAuto = False
	print("-- " + word, end="\n")
	return isAuto #Además de imprimir podés devolver algo

def return_word_and_reverse(word):
	direct = "-- " + word + " "
	reverse = "-- " + word[::-1] + "\n"
	return direct, reverse #Se puede devolver más de una cosa

#Vamos a ver qué pasa

print_word(input)
print(return_word(input))
print_reverse(input)
print(return_reverse(input))
if print_with_check(input):
	print("Me encantan los autos", end="\n")

a, b = return_word_and_reverse(input)
print(a + b, end="\n")
