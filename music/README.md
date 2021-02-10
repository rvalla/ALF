# ALF

## RandomMelodies()
With *RandomMelodies* you can create some random sequences of notes. You can produce rather a completely random
melody (*random_stream()*), one with a triangular distribution of pitches (*triangular_stream(mode_pitch)*) or one
using a control list (*control_stream()*). You pass the configuration parameters to the constructor of *RandomMelodies*
class (number of notes, number of different durations, control midi pitches list, low pitch limit, hight pitch limit).
You can see an example here:  

``` python
#import the module
from randommelodies import RandomMelodies

#create an instance
rm = RandomMelodies(100,5,[60,66,72,78], 55, 80)

#call a function
rm.aleatory_stream()
```

Feel free to contact Rodrigo by [mail](mailto:rodrigovalla@protonmail.ch) or reach him in
[telegram](https://t.me/rvalla) or [mastodon](https://fosstodon.org/@rvalla).
