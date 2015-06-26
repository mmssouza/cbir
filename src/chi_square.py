import numpy as np
import math

# @author: jonathanfriedman
def chi_square(x,y): # chi square distance
    import warnings
    warnings.filterwarnings("ignore", category = RuntimeWarning)

    acum = 0.
    for p,q in zip(x,y):
     h = (p + q)/2
     if h < 1e-12:
      h = 0
     else:
      h = ((p - h)**2)/h
     acum = acum + h
    return acum

