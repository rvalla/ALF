from adice import Dice

class DiceSet():
	"A dice set to play"

	#El estado del dado consiste en un número y una lista de líneas para dibujarlo.
	def __init__(self, n):
		self.dice = self.build_dice(n)

	def build_dice(self, n):
		d = []
		for i in range(n):
			d.append(Dice())
		return d

	#Los dados se dibujan a sí mismos...
	def __str__(self):
		m = ""
		for l in range(7):
			for d in self.dice:
				m += d.draw_line(l)
				m += " "
			m += "\n"
		return m

	#Una función para hacer trampa
	def sets(self, values):
		for v in range(len(values)):
			self.dice[v].set(values[v])

	#La función para tirar los dados
	def rolls(self):
		for d in self.dice:
			d.roll()

	#Una función para devolver los valores del conjunto de dados
	def get_dice_values(self):
		values = []
		for d in self.dice:
			values.append(d.value)
		return values
