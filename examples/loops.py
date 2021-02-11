list = [0,2,4,6,8,10]

try:
	print("- for i in list:", end="\n")
	for i in list:
		print(i, end=" ")
		print(list[i], end="\n")
	print("", end="\n")
except:
	print("Houston, we have a problem!", end="\n")
	print("", end="\n")

try:
	print("- for i in range(len(list)):", end="\n")
	for i in range(len(list)):
		print(i, end=" ")
		print(list[i], end="\n")
	print("", end="\n")
except:
	print("Houston, we have a problem!", end="\n")
	print("", end="\n")

try:
	print("- for i in enumerate(list):", end="\n")
	for i, n in enumerate(list):
		print(n, end=" ")
		print(list[i], end="\n")
	print("", end="\n")
except:
	print("Houston, we have a problem!", end="\n")
	print("", end="\n")
