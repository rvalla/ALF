import musicalscales as ms

#A list of keys to test
keys = ["Do", "Do#", "Reb", "Re", "Re#", "Mib", "Mi", "Fa", "Fa#", "Solb", "Sol", "Sol#",
		"Lab", "La", "Sib", "Si"]

#The types we want to print
types = ["major", "antique", "harmonic", "melodic"]

#Printing all scales
for k in keys:
	for t in types:
		print(k + " " + t + ": ", end="\n")
		print("--- ", end=" ")
		print(ms.print_scale_up(k, t))
		print("--- ", end=" ")
		print(ms.print_scale_down(k, t))
		print()
