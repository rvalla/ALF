import warnings
from ligeti import LigetiStorm

warnings.filterwarnings("ignore")

#Probamos una tormenta de Ligeti
title = "Un canon barullo"
composer = "Juan Pitón del Bosque"

#Vamos a partir de este motivo
pitches = [72, 73, 70, 65, 67, 76, 77, 78]
durations = [0.125, 0.25, 0.125, 0.25, 0.5, 0.125, 0.125, 0.5]

storm = LigetiStorm(title, composer, 0, "3/4", 19, 5, 0, 0.25, -3, pitches, durations)

#Si todo salió bien podemos ver la partitura
storm.show_score()

#Incluso podemos guardarla
storm.save_score("testing/", "s_test.xml", "xml")
