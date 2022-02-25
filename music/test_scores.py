import randommelodies as rmel
from scores import m21Score as m21

title = "Matriz Gruppen"
composer = "Stockhausen"

#El constructor de la clase m21Score recibe los metadatos y la armadura de clave (entero),
#el compás (string) y la cantidad de partes.
score = m21(title, composer, 0, "3/4", 12)

#Tenemos que probar las funciones propias de nuestro nuevo objeto
pitches = [1,9,2,11,10,0,6,4,5,8,3,7]
durations = [0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25]
distances = [0,4,-5,3,1,-2,6,2,-1,-3,5,-4]
for i in range(12):
	p = []
	for n in range(12):
		pitch = 60 + pitches[n] + distances[i]
		p.append(pitch)
	score.create_pitches_in_part(p, 0.25, i)

print(score)

#Si todo salió bien podemos ver la partitura
score.show_score()

#Incluso podemos guardarla
#score.save_score("testing/", "a_test.xml", "xml")
