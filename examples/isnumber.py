import random

#A little example of a try - except
number_s = input("Write a whole number: ")

try:
	number = int(number_s)
	print("You really know what a whole number is!", end="\n")
	print("You deserve I give you a greater one:", end=" ")
	print(random.randint(number + 1, 2 * number))
except:
	print("I am very confused. Is this a Turing test?", end="\n")
