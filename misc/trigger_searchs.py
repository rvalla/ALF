import time as tm
import randomsequences as rsq
import searchs as sch

#Triggering some searchs
count = 100
limit = 200
start_time = tm.monotonic() #Un tiempo de referencia en segundos

while tm.monotonic() - start_time < 3:
	l = rsq.dice_rolls(count,limit)
	l.sort()
	sch.search(rsq.dice_roll(limit), l, "binary")
