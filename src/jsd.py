import numpy as np
import scipy.stats

# @author: jonathanfriedman
def jsd(x,y): #Jensen-shannon divergence
    import warnings
    warnings.filterwarnings("ignore", category = RuntimeWarning)
#    x = np.array(x)
#    y = np.array(y)
 #   if x.max() > y.max():
 #    max = x.max()
 #   else:
 #    max = y.max()

 #   if x.min() < y.min():
 #    min = x.min()
 #   else:
 #    min = y.min()

#    h1 = scipy.stats.histogram(x,numbins = 9,defaultlimits = (0,8))
#    h2 = scipy.stats.histogram(y,numbins = 9,defaultlimits = (0,8))
#    h1 = h1[0]/h1[0].sum()
#    h2 = h2[0]/h2[0].sum()
 
    d1 = x*np.log2(2*x/(x+y))
    d2 = y*np.log2(2*y/(x+y))
    d1[np.isnan(d1)] = 0
    d2[np.isnan(d2)] = 0
    d = 0.5*np.sum(d1+d2)    
    return d

