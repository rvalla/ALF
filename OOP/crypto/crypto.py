class Crypto():
	"A simple class to encrypt text messages (to hava fun)."

	prime_list = [23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
					113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

	#El constuctor es el encargado de cargar la instancia del objeto y lo configura con los parámetros
	def __init__(self, zero_char):
		self.active_prime = 23 #El tamaño del mensaje de referencia
		self.zero_char = zero_char
		self.in_message = [] #El mensaje que hay que procesar
		self.out_message =  self.zero_char * self.active_prime #La cadena de texto que va a alojar el mensaje

	#La función que encripta el mensaje
	def encrypt(self, message, factor):
		self.in_message = [char for char in message]
		self.update(len(self.in_message))
		self.out_message = self.sort_char(self.active_prime, self.in_message, self.out_message, factor)
		m = ""
		return m.join(self.out_message)

	#La función que descifra el mensaje
	def decrypt(self, message, factor):
		self.in_message = [char for char in message]
		self.out_message = self.sort_char(self.active_prime, self.in_message, self.out_message, self.get_inverse(factor))
		m = ""
		return m.join(self.out_message)

	#La función que encripta el mensaje y deja elegir el tamaño a usar
	def custom_encrypt(self, message, size, factor):
		self.in_message = [char for char in message]
		self.out_message = self.sort_char(size, self.in_message, self.out_message, factor)
		m = ""
		return m.join(self.out_message)

	#La función que mezcla los caracteres
	def sort_char(self, size, in_message, out_message, factor):
		for i in range(len(in_message)):
			out_message[(i*factor)%size] = in_message[i]
		return self.out_message

	#La función que busca el inverso multiplicativo del factor
	def get_inverse(self, factor):
		inverse = 1
		for i in range(1, self.active_prime):
			if ((factor * i)%self.active_prime) == 1:
				inverse = i
				break
		else:
			print("Something is wrong...", end="\n")
		return inverse

	#Decidimos qué tamaño de mensaje usar necesitamos un primo p >= al tamaño del mensaje
	def update(self, size):
		for i in range(len(Crypto.prime_list)):
			if size <= Crypto.prime_list[i]:
				self.active_prime = Crypto.prime_list[i]
				break
		else:
			print("The message is huge...", end="\n")
		self.out_message = [char for char in self.zero_char * self.active_prime]

	#En Python el método __str__ te deja definir cómo se imprime en consola el objeto por defecto
	def __str__(self):
		return "Hi, I am Crypto()" + "\n" \
				+ "I am designed to encrypt text messages..." + "\n"
