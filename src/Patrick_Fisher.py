
def Patrick_Fisher(x,y):

 acum = 0
 for p,q in zip(x,y):
  acum = acum + (p - q)**2
 return acum**0.5    
