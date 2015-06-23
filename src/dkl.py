import scipy
import math
import scipy.stats

def D_KL(p,q):
 if p.max() > q.max():
  max = p.max()
 else:
  max = q.max()

 if p.min() < q.min():
  min = p.min()
 else:
  min = q.min()

 #k = math.ceil((max - min)/0.01)
 h1 = scipy.stats.histogram(p,10,defaultlimits = (min,max))
 h2 = scipy.stats.histogram(q,10,defaultlimits = (min,max))
 h1 = h1[0]/h1[0].sum()
 h2 = h2[0]/h2[0].sum()
 aux = (h1 + h2)/2
 
 return (scipy.stats.entropy(h1,aux) + scipy.stats.entropy(h2,aux))/2
