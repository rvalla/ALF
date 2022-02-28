import randommelodies as rmel
from scores import m21Score as m21
import random as rd

title = "Homenaje a Ferneyhough"
composer = "Complex Ity"

#El constructor de la clase m21Score recibe los metadatos y la armadura de clave (entero),
#el compás (string) y la cantidad de partes.
score = m21(title, composer, 0, "3/4", 4)

notes = [-1,-1,-1,-1,0,0,0,0,0,2,2,4,4,4,4,5,6,7,7,7,7,7,9,9,10,11]
sizes = [3,3,3,5,5,5,6,6,6,7,9,10,11]

for i in range(score.parts_count):
	for t in range(30):
		if rd.random() < 0.65:
			size = rd.choice(sizes)
			n = [(rd.choice(notes) + 79 - i * 12) for j in range(size)]
			score.create_tuplet_in_part(n, i)
		else:
			size = rd.choice([1,1,1,2,2,2,4])
			n = [(rd.choice(notes) + 79 - i * 12) for j in range(size)]
			d = [1 / size for j in range(size)]
			score.create_notes_in_part(n, d, i)


print(score)

#Si todo salió bien podemos ver la partitura
score.show_score()

#Incluso podemos guardarla
#score.save_score("testing/", "a_test.xml", "xml")
