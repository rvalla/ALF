from adice import Dice
from diceset import DiceSet

#Vamos a probar las primeras clases para hacer juegos de dados
print("-- Vamos con Dice:", end="\n")
d = Dice()
print(d)
d.roll()
print(d)
d.set(3)
print(d)
print("", end="\n")

print("-- Vamos con DiceSet:", end="\n")
s = DiceSet(5)
print(s)
s.roll_all()
print(s)
s.roll_one(3)
print(s)
s.roll_some([0,4])
print(s)
s.set_all([1,2,3,4,5])
print(s)
s.set_some([1,1], [1,3])
print(s)
s.set_one(0,6)
print(s)
print("", end="\n")
