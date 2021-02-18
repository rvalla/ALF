import random as rd

#Rolling a dice
def dice_roll(f):
	return rd.randint(1,f)

#A sequence of dice rolls
def dice_rolls(n, f):
	l = []
	for r in range(n):
		l.append(dice_roll(f))
	return l
