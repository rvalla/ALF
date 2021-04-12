import randommelodies as rmel
from scores import m21Score as m21

title = "Esta melodía te vuela la cabeza"
composer = "Juan Pitón del Bosque"

#El constructor de la clase m21Score recibe los metadatos y la armadura de clave (entero),
#el compás (string) y la cantidad de partes.
score = m21(title, composer, 3, "4/4", 3)

#Ahora vamos a probar si realmente funciona.
score.add_notes_to_part(rmel.random_stream(25, 6, 58, 72), 0)
score.add_notes_to_part(rmel.control_stream(20, 2, [48,52,55,48,48]), 1)

#Tenemos que probar las funciones propias de nuestro nuevo objeto
pitches = [-1,36,37,38,39,40,41,-1]
durations = [1,0.5,0.25,0.5,0.25,1,1,1]
score.create_pitches_in_part(pitches, 0.25, 2)
score.create_notes_in_part(pitches, durations, 2)

print(score)

#Si todo salió bien podemos ver la partitura
score.show_score()

#Incluso podemos guardarla
score.save_score("testing/", "a_test.xml", "xml")
