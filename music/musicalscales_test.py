import musicalscales as ms

keys = ["Do", "Do#", "Reb", "Re", "Re#", "Mib", "Mi", "Fa", "Fa#", "Solb", "Sol", "Sol#",
				"Lab", "La", "Sib", "Si"]
types = ["major", "antique", "harmonic"]

for k in keys:
	for t in types:
		print(k + " " + t + ": ", end="\n")
		print("--- ", end=" ")
		print(ms.print_scale_up(k, t))
		print("--- ", end=" ")
		print(ms.print_scale_down(k, t))
		print()
