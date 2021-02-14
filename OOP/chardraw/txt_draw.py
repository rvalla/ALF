import random as rd
from char_draw import CharDraw

class TxtDraw(CharDraw):
	"A simple class to draw some fun things to txt files"

	#El constuctor es el encargado de cargar la instancia del objeto y lo configura con los parámetros
	def __init__(self, file_name, width, margin, step, circle_fraction, w_char, b_char):
		self.file_name = file_name #Agregamos un nombre de archivo al constructor de CharDraw
		self.file_path = "output/" #Agregamos una ruta
		self.file_count = 0 #Diferenciamos los archivos
		CharDraw.__init__(self, width, margin, step, circle_fraction, w_char, b_char)

	#La función que dibuja n líneas aleatorias
	def random_draw(self, lines):
		self.file_count += 1
		file = open(self.file_path + self.file_name + "_" + str(self.file_count) + ".txt", "w")
		for i in range(lines):
			r = rd.randint(1, self.width) #Primero pedimos un número al azar menor que self.width
			file.write(self.draw_line(self.margin, r, self.width - r)) #Llama a la función que dibuja una línea n veces
			file.write("\n") #Agregamos el salto de línea
		file.close()

	#La función que dibuja n líneas aleatorias con una distribución triangular
	def triangular_draw(self, lines):
		self.file_count += 1
		file = open(self.file_path + self.file_name + "_" + str(self.file_count) + ".txt", "w")
		for i in range(lines):
			r = int(rd.triangular(1, self.width, self.width//2))
			file.write(self.draw_line(self.margin, r, self.width - r)) #Llama a la función que dibuja una línea n veces
			file.write("\n") #Agregamos el salto de línea
		file.close()

	#La función para dibujar una onda sinusoidal
	def sin_draw(self, lines):
		self.file_count += 1
		file = open(self.file_path + self.file_name + "_" + str(self.file_count) + ".txt", "w")
		a = 0 #El ángulo
		w = self.width//2 #Dividimos el ancho en 2
		for i in range(lines):
			b = w + self.translate_sin(a, w)
			file.write(self.draw_line(self.margin, b, self.width - b)) #Llama a la función que dibuja una línea n veces
			a += self.angle
			file.write("\n") #Agregamos el salto de línea
		file.close()

	#La función para dibujar una onda compleja
	def harmonic_draw(self, lines, harmonics):
		self.file_count += 1
		file = open(self.file_path + self.file_name + "_" + str(self.file_count) + ".txt", "w")
		a = 0 #El ángulo fundamental
		w = self.width//2 #Dividimos el ancho en 2
		for i in range(lines):
			b = w
			for h in harmonics:
				b += self.translate_sin(a*h, w//(1 + h))
			file.write(self.draw_line(self.margin, b, self.width - b)) #Llama a la función que dibuja una línea n veces
			a += self.angle
			file.write("\n") #Agregamos el salto de línea
		file.close()

	#La función que dibuja n líneas de zigzag
	def zigzag_draw(self, lines):
		self.file_count += 1
		file = open(self.file_path + self.file_name + "_" + str(self.file_count) + ".txt", "w")
		d = 1 #La dirección del movimiento
		p = 0 #La posición
		for i in range(lines):
			file.write(self.draw_line(self.margin, p, self.width - p)) #Llama a la función que dibuja una línea n veces
			p += d * self.step #Actualizamos la posición
			if p > self.width - self.step: #Chequeamos si tiene que cambiar la dirección
				d = -1
			elif p < 1:
				d = 1
			file.write("\n") #Agregamos el salto de línea
		file.close()
