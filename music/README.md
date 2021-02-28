# ALF

## randommelodies.py
With *randommelodies.py* you can create some random sequences of notes. You can use the following functions:

- *random_stream(count, durations, low_l, high_l)*: produce a completely random melody of *count* notes, each one
with one of a desire number of *durations*. The pitches will be between *low_l* and *high_l*.  
- *triangular_stream(count, durations, low_l, high_l, mode)*: produce a melody its pitch values have a triangular
distribution, each one with one of a desire number of *durations*.  
- *control_stream(count, durations, [pitch_values])*: produce a melody choosing the notes randomly from *pitch_values*
list, each one with one of a desire number of *durations*.  

``` python
#import the module
import randommelodies as rm

#call a function
rm.aleatory_stream(100, 4, 50, 60)
```
## musicalscales.py
In *musicalscales* the challenge was to create functions to obtain the list of notes of a musical scale. You can see
other solutions in *BuscarEscalas.py* and *ArmaEscalasNxN.py*...   

## circlemelodies.py
Functions to make a melody iterating a list of pitches and duration values a complete cycle.

```python
#import the module
import circlemelodies as cm

#Take a note list in midi values
notes = [60, 62, 64, 62, 60]

#Take a duration list in floats (1 is a quarter note)
durations = [0.5, 0.25, 1, 0.5]

#call the function
cm.circle_melody(notes, durations)
```

Feel free to contact Rodrigo by [mail](mailto:rodrigovalla@protonmail.ch) or reach him in
[telegram](https://t.me/rvalla) or [mastodon](https://fosstodon.org/@rvalla).
