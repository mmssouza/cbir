import numpy as np
import math

# @author: jonathanfriedman
def He(x,y): # Hellinger distance
    import warnings
    warnings.filterwarnings("ignore", category = RuntimeWarning)

    acum = 0.
    for p,q in zip(x,y):
     acum = acum + (math.sqrt(p) - math.sqrt(q))**2
    acum = acum/2
    acum = math.sqrt(acum)
    return acum

