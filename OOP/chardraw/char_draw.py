import random as rd
import math as mth

class CharDraw():
	"A simple class to draw some fun things using text"

	#El constuctor es el encargado de cargar la instancia del objeto y lo configura con los parámetros
	def __init__(self, width, margin, step, circle_fraction, w_char, b_char):
		self.width = width
		self.margin = margin
		self.step = step
		self.angle = round(mth.pi * 2 / circle_fraction, 4)
		self.w_char = w_char
		self.b_char = b_char

	#La función que dibuja n líneas aleatorias
	def random_draw(self, lines):
		for i in range(lines):
			r = rd.randint(1, self.width) #Primero pedimos un número al azar menor que self.width
			print(self.draw_line(self.margin, r, self.width - r)) #Llama a la función que dibuja una línea n veces

	#La función que dibuja n líneas aleatorias con una distribución triangular
	def triangular_draw(self, lines):
		for i in range(lines):
			r = int(rd.triangular(1, self.width, self.width//2))
			print(self.draw_line(self.margin, r, self.width - r)) #Llama a la función que dibuja una línea n veces

	#La función para dibujar una onda sinusoidal
	def sin_draw(self, lines):
		a = 0 #El ángulo
		w = self.width//2 #Dividimos el ancho en 2
		for i in range(lines):
			b = w + self.translate_sin(a, w)
			print(self.draw_line(self.margin, b, self.width - b)) #Llama a la función que dibuja una línea n veces
			a += self.angle

	#La función para dibujar una onda compleja
	def harmonic_draw(self, lines, harmonics):
		a = 0 #El ángulo fundamental
		w = self.width//2 #Dividimos el ancho en 2
		for i in range(lines):
			b = w
			for h in harmonics:
				b += self.translate_sin(a*h, w//(1 + h))
			print(self.draw_line(self.margin, b, self.width - b)) #Llama a la función que dibuja una línea n veces
			a += self.angle

	#Una mapear sin(a) a un ancho en caracteres
	def translate_sin(self, a, w):
		return int(mth.sin(a) * w)

	#La función que dibuja n líneas de zigzag
	def zigzag_draw(self, lines):
		d = 1 #La dirección del movimiento
		p = 0 #La posición
		for i in range(lines):
			print(self.draw_line(self.margin, p, self.width - p)) #Llama a la función que dibuja una línea n veces
			p += d * self.step #Actualizamos la posición
			if p > self.width - self.step: #Chequeamos si tiene que cambiar la dirección
				d = -1
			elif p < 1:
				d = 1

	#La función que dibuja una línea
	def draw_line(self, m, b, w):
		line = self.draw_link(" ", m) #Constuimos el margen
		line += self.draw_link(self.b_char, b) #Le sumamos b caracteres negros
		line += self.draw_link(self.w_char, w) #Le sumamos w caracteres blancos
		return line

	#La función que dibuja porciones de líneas
	def draw_link(self, char, width):
		return char * width

	#En Python el método __str__ te deja definir cómo se imprime en consola el objeto por defecto
	def __str__(self):
		return "Hi, I am CharDraw()" + "\n" \
				+ "I am designed to draw with text..." + "\n" \
				+ "My actual configuration is:" + "\n" \
				+ "- width: " + str(self.width) + "\n" \
				+ "- margin: " + str(self.margin) + "\n" \
				+ "- step: " + str(self.step) + "\n" \
				+ "- angle: " + str(self.angle) + "\n" \
				+ "- white char: " + str(self.w_char) + "\n" \
				+ "- black char: " + str(self.b_char)
