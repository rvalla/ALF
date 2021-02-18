import math as mth

#Some alternatives to search on a list

#If we know the list is in order the binary search is the best option
#We need a list of 2^n elements
def binary_list(list):
	ls = list
	last = list[len(list) - 1]
	while not mth.sqrt(len(ls)).is_integer():
		ls.append(last)
	return ls

#Looking for an element in the list
def binary_search(element, list):
	center = len(list) // 2 - 1
	if len(list) == 1:
		return element == list[center]
	else:
		if element == list[center]:
			return True
		elif element > list[center]:
			return binary_search(element, list[center + 1:])
		elif element < list[center]:
			return binary_search(element, list[:center + 1])

#Para imprimir un resultado elegante
def search(element, list, type):
	print("Checking if " + str(element) + " is in " + str(list), end="\n")
	isIn = False
	#Elegimos el tipo de búsqueda
	if type == "binary":
		isIn = binary_search(element, binary_list(list))
	#Imprimimos el resultado
	if isIn:
		print("I found " + str(element) + ". It was there...", end="\n")
	else:
		print("Nop. It is not.", end="\n")
